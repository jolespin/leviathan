#!/usr/bin/env python
import sys, os, time, gzip, bz2, subprocess, pickle, json, logging, functools, hashlib
from datetime import datetime
import pathlib
from tqdm import tqdm
from collections import defaultdict
from memory_profiler import memory_usage
from pandas.errors import EmptyDataError

# Read/Write
# ==========
# Get file object
def open_file_reader(filepath: str, compression="auto", binary=False):
    """
    Opens a file for reading with optional compression.

    Args:
        filepath (str): Path to the file.
        compression (str, optional): Type of compression {None, 'gzip', 'bz2'}. Defaults to "auto".
        binary (bool, optional): Whether to open the file in binary mode. Defaults to False.

    Returns:
        file object: A file-like object.
    """
    # Determine compression type based on the file extension if 'auto' is specified
    if compression == "auto":
        ext = filepath.split(".")[-1].lower()
        if ext == "gz":
            compression = "gzip"
        elif ext == "bz2":
            compression = "bz2"
        else:
            compression = None

    # Determine the mode based on the 'binary' flag
    mode = "rb" if binary else "rt"

    # Open the file with or without compression
    if not compression:
        return open(filepath, mode)
    elif compression == "gzip":
        return gzip.open(filepath, mode)
    elif compression == "bz2":
        return bz2.open(filepath, mode)
    else:
        raise ValueError(f"Unsupported compression type: {compression}")
            
# Get file object
def open_file_writer(filepath: str, compression="auto", binary=False):
    """
    Args:
        filepath (str): path/to/file
        compression (str, optional): {None, gzip, bz2}. Defaults to "auto".
        binary (bool, optional): Whether to open the file in binary mode. Defaults to False.
    
    Returns:
        file object
    """
    if compression == "auto":
        ext = filepath.split(".")[-1].lower()
        if ext == "gz":
            compression = "gzip"
        elif ext == "bz2":
            compression = "bz2"
        else:
            compression = None

    if binary:
        mode = "wb"
    else:
        mode = "wt"

    if not compression:
        return open(filepath, mode)
    elif compression == "gzip":
        return gzip.open(filepath, mode)
    elif compression == "bz2":
        return bz2.open(filepath, mode)
    else:
        raise ValueError(f"Unsupported compression type: {compression}")

# Pickle I/O
def read_pickle(filepath, compression="auto"):
    with open_file_reader(filepath, compression=compression, binary=True) as f:
        return pickle.load(f)
    
def write_pickle(obj, filepath, compression="auto"):
    with open_file_writer(filepath, compression=compression, binary=True) as f:
        pickle.dump(obj, f)
        
# Json I/O
def read_json(filepath):
    with open_file_reader(filepath, compression=None, binary=False) as f:
        return json.load(f)
    
def write_json(obj, filepath, indent=4):
    with open_file_writer(filepath, compression=None, binary=False) as f:
        return json.dump(obj, f)
    
# Annotations
def read_annotations(path:str, format="pykofamsearch"):
    choices = {"pykofamsearch", "pyhmmsearch", "veba-pfam","veba-kofam","veba-cazy","veba-uniref", "veba-mibig", "veba-vfdb","veba-amr", "custom"}
    if format not in choices:
        raise KeyError(f"format must be in {choices}")
    
    if format in {"pykofamsearch", "pyhmmsearch", "custom"}:
        f_annotations = open_file_reader(path)

        gene_to_features = defaultdict(set)    
        if format != "custom":
            next(f_annotations)
        for line in tqdm(f_annotations, desc="Extracting feature annotations"):
            line = line.strip()
            if line:
                id_gene, id_feature, *extra = line.split("\t")
                gene_to_features[id_gene].add(id_feature)
        f_annotations.close()
    else:
        from pandas import read_csv
        df_annotations = read_csv(path, sep="\t", index_col=0, header=[0,1])
        
        # HMM-based annotations
        if format in {"veba-pfam", "veba-kofam", "veba-amr"}:
            column = {
                "veba-pfam":("Pfam", "ids"),
                "veba-kofam":("KOfam", "ids"),
                "veba-amr":("NCBIfam-AMR", "ids"),
            }[format]
            gene_to_features = df_annotations[column].map(lambda x: set(eval(x)))
        
        # Diamond-based annotations
        else:
            column = {
                "veba-cazy":("CAZy", "sseqid"),
                "veba-uniref":("UniRef", "sseqid"),
                "veba-mibig":("MIBiG", "sseqid"),
                "veba-vfdb":("VFDB", "sseqid"),
            }[format]
            
            gene_to_features = defaultdict(set)
            for id_gene, id_feature in df_annotations[column].items():
                gene_to_features[id_gene].add(id_feature)
    return gene_to_features

# Formatting
# ==========
# Get duration
def format_duration(duration):
    """
    Format the elapsed time since `t0` in hours, minutes, and seconds.
    
    Adapted from @john-fouhy:
    https://stackoverflow.com/questions/538666/python-format-timedelta-to-string
    """
    hours, remainder = divmod(int(duration), 3600)
    minutes, seconds = divmod(remainder, 60)
    return f"{hours:02}:{minutes:02}:{seconds:02}"

# Format header for printing
def format_header(text, line_character="=", n=None):
    if n is None:
        n = len(text)
    line = n*line_character
    return "{}\n{}\n{}".format(line, text, line)

# Format memory
def format_bytes(B, unit="auto", return_units=True):
    """
    Return the given bytes as a human-readable string in KB, MB, GB, or TB.
    1 KB = 1024 Bytes

    Adapted from the following source (@whereisalext):
    https://stackoverflow.com/questions/12523586/python-format-size-application-converting-b-to-kb-mb-gb-tb/52379087
    """
    KB = 1024
    MB = KB ** 2  # 1,048,576
    GB = KB ** 3  # 1,073,741,824
    TB = KB ** 4  # 1,099,511,627,776

    def format_with_unit(size, unit_name):
        return f"{size:.2f} {unit_name}" if return_units else size

    unit = unit.lower()
    if unit != "auto":
        unit = unit.lower()
        if unit == "b":
            return format_with_unit(B, "B")
        elif unit == "kb":
            return format_with_unit(B / KB, "KB")
        elif unit == "mb":
            return format_with_unit(B / MB, "MB")
        elif unit == "gb":
            return format_with_unit(B / GB, "GB")
        elif unit == "tb":
            return format_with_unit(B / TB, "TB")
        else:
            raise ValueError(f"Unknown unit: {unit}")
    else:
        if B < KB:
            return format_with_unit(B, "B")
        elif KB <= B < MB:
            return format_with_unit(B / KB, "KB")
        elif MB <= B < GB:
            return format_with_unit(B / MB, "MB")
        elif GB <= B < TB:
            return format_with_unit(B / GB, "GB")
        else:
            return format_with_unit(B / TB, "TB")
        
# Logging
# =======
def build_logger(logger_name=__name__, stream=sys.stdout):
    # Create a logger object
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.DEBUG)  # Set the logging level
    
    # Create a stream handler to output logs to stdout
    stream_handler = logging.StreamHandler(stream)
    stream_handler.setLevel(logging.DEBUG)  # Set the level for the handler
    
    # Create a formatter and set it to the handler
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    stream_handler.setFormatter(formatter)
    
    # Add the handler to the logger
    logger.addHandler(stream_handler)

    return logger
    
def reset_logger(logger):
    # Remove all existing handlers
    for handler in logger.handlers[:]:
        logger.removeHandler(handler)
        handler.close()
    
    # Set a new handler (for example, to output to stdout)
    stream_handler = logging.StreamHandler(sys.stdout)
    stream_handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)
    
    # Optionally set a new level
    logger.setLevel(logging.DEBUG)
    
# Timestamp
def get_timestamp(format_string:str="%Y-%m-%d %H:%M:%S"):
    # Get the current date and time
    now =  datetime.now()
    # Create a timestamp string
    return now.strftime(format_string)

# Profiling
# =========
def profile_peak_memory(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Measure memory usage
        mem_usage = memory_usage((func, args, kwargs), max_usage=True, retval=True, max_iterations=1)
        peak_memory, result = mem_usage[0], mem_usage[1]
        print(f"Peak memory usage for {func.__name__}: {format_bytes(peak_memory)}")
        return result
    return wrapper

# Directory
# =========
def get_file_size(filepath:str, format=False):
    size_in_bytes = os.stat(filepath).st_size
    if format:
        return format_bytes(size_in_bytes)
    else:
        return size_in_bytes
    
def check_file(filepath:str, empty_ok=False, minimum_filesize=1): # Doesn't handle empty gzipped files
    if not os.path.exists(filepath):
        raise FileNotFoundError(filepath)
    if not empty_ok:
        if get_file_size(filepath) < minimum_filesize:
            raise EmptyDataError(filepath)

# md5 hash from file
def get_md5hash_from_file(filepath:str, block_size=65536):
    """
    Calculate the MD5 hash of a file.

    Parameters:
    - file_path: The path to the file.
    - block_size: The size of each block read from the file (default is 64KB).

    Returns:
    - A string containing the MD5 hash.
    """
    md5 = hashlib.md5()
    with open(filepath, 'rb') as f:
        for block in iter(lambda: f.read(block_size), b''):
            md5.update(block)
    return md5.hexdigest()

# md5 hash from directory
def get_md5hash_from_directory(directory:str):
    """
    Calculate the MD5 hash of all files in a directory.

    Parameters:
    - directory_path: The path to the directory.

    Returns:
    - A dictionary where the keys are file paths and the values are their MD5 hashes.
    """
    md5_hashes = {}
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            if os.path.isfile(file_path):
                file_md5 = get_md5hash_from_file(file_path)
                md5_hashes[file_path] = file_md5
    return md5_hashes

# Get directory tree structure
def get_directory_tree(root, ascii=False):
    if not ascii:
        return DisplayablePath.view(root)
    else:
        return DisplayablePath.get_ascii(root)

# Directory size
def get_directory_size(directory:str='.'):
    """
    Adapted from @Chris:
    https://stackoverflow.com/questions/1392413/calculating-a-directorys-size-using-python
    """

    total_size = 0
    seen = {}
    for dirpath, dirnames, filenames in os.walk(directory):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            try:
                stat = os.stat(fp)
            except OSError:
                continue

            try:
                seen[stat.st_ino]
            except KeyError:
                seen[stat.st_ino] = True
            else:
                continue

            total_size += stat.st_size

    return total_size


# Classes
# =======
class RunShellCommand(object):
    """
    Args: 
        command:str command to be executed
        name:str name associated with command [Default: None]
        shell_executable:str path to executable [Default: /bin/bash]
        
    Usage: 
        cmd = RunShellCommand("time (sleep 5 & echo 'Hello World')", name="Demo")
        cmd.run()
        cmd
        # ================================================
        # RunShellCommand(name:Demo)
        # ================================================
        # (/bin/bash)$ time (sleep 5 & echo 'Hello World')
        # ________________________________________________
        # Properties:
        #     - stdout: 61.00 B
        #     - stderr: 91.00 B
        #     - returncode: 0
        #     - peak memory: 37.22 B
        #     - duration: 00:00:05

    """

    def __init__(
        self, 
        command:str, 
        name:str=None, 
        shell_executable:str="/bin/bash",
        validate_input_filepaths:list=None,
        validate_output_filepaths:list=None,
        ):

        if isinstance(command, str):
            command = [command]
        command = " ".join(list(filter(bool, map(str, command))))
        self.command = command
        self.name = name
        self.shell_executable = shell_executable
        self.validate_input_filepaths = validate_input_filepaths if validate_input_filepaths else list()
        self.validate_output_filepaths = validate_input_filepaths if validate_input_filepaths else list()
        self.executed = False
        
    def run(self, stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding="utf-8", **popen_kws):
        def execute_command(encoding, stdout, stderr):
            # Execute the process
            self.process_ = subprocess.Popen(
                self.command,
                shell=True,
                stdout=stdout,
                stderr=stderr,
                executable=self.shell_executable,
                **popen_kws,
            )
            # Wait until process is complete and return stdout/stderr
            self.stdout_, self.stderr_ = self.process_.communicate()
            self.returncode_ = self.process_.returncode
            
            # Encode
            if encoding:
                if self.stdout_:
                    self.stdout_ = self.stdout_.decode(encoding)
                if self.stderr_:
                    self.stderr_ = self.stderr_.decode(encoding)

        # I/O
        self.redirect_stdout = None
        if isinstance(stdout, str):
            self.redirect_stdout = stdout
            stdout = open(stdout, "wb")

        self.redirect_stderr = None
        if isinstance(stderr, str):
            self.redirect_stderr = stderr
            stderr = open(stderr, "wb")

        # Measure memory usage
        t0 = time.time()
        if self.validate_input_filepaths:
            for filepath in self.validate_input_filepaths:
                check_file(filepath, empty_ok=False)
        self.memory_usage_ = memory_usage((execute_command, (encoding, stdout, stderr,)), max_iterations=1)
        self.duration_ = time.time() - t0

        # # Flush
        # if hasattr(stdout, "flush"):
        #     stdout.flush()
        # if hasattr(stderr, "flush"):
        #     stderr.flush()
            
        # Close
        if hasattr(stdout, "close"):
            stdout.close()
        if hasattr(stderr, "close"):
            stderr.close()

        self.peak_memory_ = max(self.memory_usage_)
        self.executed = True

        return self

    def __repr__(self):
        name_text = "{}(name:{})".format(self.__class__.__name__, self.name)
        command_text = "({})$ {}".format(self.shell_executable, self.command)
        n = max(len(name_text), len(command_text))
        pad = 4
        fields = [
            format_header(name_text,line_character="=", n=n),
            *format_header(command_text, line_character="_", n=n).split("\n")[1:],
            ]
        if self.executed:
            fields += [
            "Properties:",
            ]
            # stdout
            if self.redirect_stdout:
                fields += [
                pad*" " + "- stdout({}): {}".format(
                    self.redirect_stdout,
                    get_file_size(self.redirect_stdout, format=True),
                )
                ]
            else:
                fields += [
                pad*" " + "- stdout: {}".format(format_bytes(sys.getsizeof(self.stdout_))),
                ]
            # stderr
            if self.redirect_stderr:
                fields += [
                pad*" " + "- stderr({}): {}".format(
                    self.redirect_stderr,
                    get_file_size(self.redirect_stderr, format=True),
                )
                ]
            else:
                fields += [
                pad*" " + "- stderr: {}".format(format_bytes(sys.getsizeof(self.stderr_))),
                ]

            fields += [
            pad*" " + "- returncode: {}".format(self.returncode_),
            pad*" " + "- peak memory: {}".format(format_bytes(self.peak_memory_)),
            pad*" " + "- duration: {}".format(format_duration(self.duration_)),
            ]
        return "\n".join(fields)
    
    # Dump stdout, stderr, and returncode
    def dump(self, output_directory:str):    
        # stdout
        with open_file_writer(os.path.join(output_directory, f"{self.name}.o")) as f:
            print(self.stdout_, file=f)
        # stderr
        with open_file_writer(os.path.join(output_directory, f"{self.name}.e")) as f:
            print(self.stderr_, file=f)
        # returncode
        with open_file_writer(os.path.join(output_directory, f"{self.name}.returncode")) as f:
            print(self.returncode_, file=f)
            
    # Check status
    def check_status(self):
        if self.returncode_ != 0:
            raise subprocess.CalledProcessError(
                returncode=self.returncode_,
                cmd="\n".join([
                f"Command Failed: {self.command}",
                f"return code: {self.returncode_}",
                f"stderr:\n{self.stderr_}",
                ]),
            )
        else:
            if self.validate_output_filepaths:
                for filepath in self.validate_output_filepaths:
                    check_file(filepath, empty_ok=False)
            print(f"Command Successful: {self.command}", file=sys.stderr)

# # View directory structures
class DisplayablePath(object):
    """
    Source: https://github.com/jolespin/genopype
    
    Display the tree structure of a directory.

    Implementation adapted from the following sources:
        * Credits to @abstrus
        https://stackoverflow.com/questions/9727673/list-directory-tree-structure-in-python
    """
    display_filename_prefix_middle = '|__'
    display_filename_prefix_last = '|__'
    display_parent_prefix_middle = '    '
    display_parent_prefix_last = '|   '

    def __init__(self, path, parent_path, is_last):
        self.path = pathlib.Path(str(path))
        self.parent = parent_path
        self.is_last = is_last
        if self.parent:
            self.depth = self.parent.depth + 1
        else:
            self.depth = 0

    @property
    def displayname(self):
        if self.path.is_dir():
            return self.path.name + '/'
        return self.path.name

    @classmethod
    def make_tree(cls, root, parent=None, is_last=False, criteria=None):
        root = pathlib.Path(str(root))
        criteria = criteria or cls._default_criteria

        displayable_root = cls(root, parent, is_last)
        yield displayable_root

        children = sorted(list(path
                               for path in root.iterdir()
                               if criteria(path)),
                          key=lambda s: str(s).lower())
        count = 1
        for path in children:
            is_last = count == len(children)
            if path.is_dir():
                for item in cls.make_tree(path, parent=displayable_root, is_last=is_last, criteria=criteria):
                    yield item
            else:
                yield cls(path, displayable_root, is_last)
            count += 1

    @classmethod
    def _default_criteria(cls, path):
        return True

    @property
    def displayname(self):
        if self.path.is_dir():
            return self.path.name + '/'
        return self.path.name

    def displayable(self):
        if self.parent is None:
            return self.displayname

        _filename_prefix = (self.display_filename_prefix_last
                            if self.is_last
                            else self.display_filename_prefix_middle)

        parts = ['{!s} {!s}'.format(_filename_prefix,
                                    self.displayname)]

        parent = self.parent
        while parent and parent.parent is not None:
            parts.append(self.display_parent_prefix_middle
                         if parent.is_last
                         else self.display_parent_prefix_last)
            parent = parent.parent

        return ''.join(reversed(parts))

    # Additions by Josh L. Espinoza for Soothsayer
    @classmethod
    def get_ascii(cls, root):
        ascii_output = list()
        paths = cls.make_tree(root)
        for path in paths:
            ascii_output.append(path.displayable())
        return "\n".join(ascii_output)
    @classmethod
    def view(cls, root, file=sys.stdout):
        print(cls.get_ascii(root), file=file)
