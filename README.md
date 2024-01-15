
# SimonicLang Programming Language

SimonicLang is a simple and versatile programming language designed for various scripting tasks. This README provides an overview of the language and instructions on how to use the SimonicLang compiler (`SLCompiler.exe`).

## Features

- **Command Set:** SimonicLang offers a wide range of commands and functions for tasks such as file manipulation, web interactions, system information retrieval, and more.
- **F-String Support:** Utilize F-Strings for efficient string formatting in your SimonicLang code.

## Getting Started

### Prerequisites

- SimonicLang Compiler (`SLCompiler.exe`)
- Python with Tkinter for GUI compilation

### Installing

1. Install git
2. Open cmd and enter: ```git clone https://github.com/aertsimon90/SimonicLang```

### Usage

#### Running SimonicLang Script

1. Open a terminal or command prompt.
2. Navigate to the directory containing your SimonicLang script and `simlang.py`.
3. Run the script with the following command:

   ```bash
   python simlang.py your_script.sl
   ```

   Replace `your_script.sl` with the name of your SimonicLang script.

#### Compiling with GUI

1. Run the SimonicLang Compiler GUI using the following command:

   ```bash
   SLCompiler.exe
   ```

   This requires Python with Tkinter.

#### Compiling with Batch Script

1. Run the setup batch script using the following command:

   ```bash
   setup.bat
   ```

   This will set up the necessary dependencies for GUI compilation.

2. After running the setup, you can compile SimonicLang scripts using the GUI.

## Example

Here's a simple example of a SimonicLang script:

```simoniclang
log;Hello World!$<n>
logf;$<c.red>This text is red!$<c.reset>$<n>
vSet;loopNum;0
loop;5;math;$<v.loopNum>+1;loopNum && inputf;cmd;This your is $<v.loopNum>. Command:  && runCmd;$<v.cmd>
```

## Documentation

For a detailed list of commands, F-string usage, and other features, refer to the [SimonicLang Documentation](https://github.com/aertsimon90/SimonicLang/blob/main/documentation.txt).

## License

This project is licensed under the [MIT License](https://github.com/aertsimon90/SimonicLang/blob/main/LICENSE).

## Acknowledgments

- Special thanks to Simon Scap for contributing to the development of SimonicLang.
