#!/usr/bin/env python
import sys, os, time, gzip, bz2, subprocess, pickle, json, logging
from memory_profiler import memory_usage

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
def format_memory(B, unit="auto", return_units=True):
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
        ):

        if isinstance(command, str):
            command = [command]
        command = " ".join(list(filter(bool, map(str, command))))
        self.command = command
        self.name = name
        self.shell_executable = shell_executable
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
                    format_memory(os.stat(self.redirect_stdout).st_size),
                )
                ]
            else:
                fields += [
                pad*" " + "- stdout: {}".format(format_memory(sys.getsizeof(self.stdout_))),
                ]
            # stderr
            if self.redirect_stderr:
                fields += [
                pad*" " + "- stderr({}): {}".format(
                    self.redirect_stderr,
                    format_memory(os.stat(self.redirect_stderr).st_size),
                )
                ]
            else:
                fields += [
                pad*" " + "- stderr: {}".format(format_memory(sys.getsizeof(self.stderr_))),
                ]

            fields += [
            pad*" " + "- returncode: {}".format(self.returncode_),
            pad*" " + "- peak memory: {}".format(format_memory(self.peak_memory_)),
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
                "\n".join([
                f"Command Failed: {self.command}",
                f"return code: {self.return_code_}",
                f"stderr:\n{self.stderr_}",
                ]),
            )
        else:
            print(f"Command Successful: {self.command}", file=sys.stderr)
