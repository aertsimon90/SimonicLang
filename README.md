
# SimonicLang Programming Language

SimonicLang is a simple and versatile programming language designed for various scripting tasks. This README provides an overview of the language and instructions on how to use the SimonicLang compiler (`SLCompiler.exe`).

## Features

- **Command Set:** SimonicLang offers a wide range of commands and functions for tasks such as file manipulation, web interactions, system information retrieval, and more.
- **F-String Support:** Utilize F-Strings for efficient string formatting in your SimonicLang code.

## Getting Started

### Prerequisites

- SimonicLang Compiler (`SLCompiler.exe`)

### Installing

1. Download the SimonicLang Compiler from [GitHub Releases](https://github.com/aertsimon90/SimonicLang/releases).
2. Extract the contents of the downloaded archive.

### Usage

1. Open a terminal or command prompt.
2. Navigate to the directory containing your SimonicLang script and `SLCompiler.exe`.
3. Run the compiler with the following command:

   ```bash
   SLCompiler.exe your_script.sl
   ```

   Replace `your_script.sl` with the name of your SimonicLang script.

4. The compiler will generate the executable output.

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

- Special thanks to [Your Name] for contributing to the development of SimonicLang.
