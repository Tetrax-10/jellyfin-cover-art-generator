# Jellyfin Cover Art generator

Generates cover art for Jellyfin library in batch

## Demo

<table>
  <tr align="center">
    <td><img src="https://raw.githubusercontent.com/Tetrax-10/jellyfin-cover-art-generator/main/assets/Movies-dune.jpg" style="width: 400px;"></td>
    <td><img src="https://raw.githubusercontent.com/Tetrax-10/jellyfin-cover-art-generator/main/assets/TV Shows-chernobyl.jpg" style="width: 400px;"></td>
  </tr>
  <tr align="center">
    <td><img src="https://raw.githubusercontent.com/Tetrax-10/jellyfin-cover-art-generator/main/assets/Music.jpg" style="width: 400px;"></td>
    <td><img src="https://raw.githubusercontent.com/Tetrax-10/jellyfin-cover-art-generator/main/assets/xxx.jpg" style="width: 400px;"></td>
  </tr>
</table>

</br>

**Run `coverart` in terminal without any arguments (flags) to initiate interactive prompts.**

![demo preview](https://raw.githubusercontent.com/Tetrax-10/jellyfin-cover-art-generator/main/assets/preview.png)

**Note:** This Screenshot reflects initial release and new changes may not be represented.

</br>

## CLI docs

You can use this as a CLI by just giving a valid argument(s).

The above movies cover art can be created with this command.

```powershell
coverart -p "dune.jpg" -t "Movies"
```

### Arguments

<table>
  <tr align="center">
    <td><b>args</b></td>
    <td><b>Full args</b></td>
    <td><b>Description</b></td>
    <td><b>Default</b></td>
    <td><b>Type</b></td>
  </tr>
  <tr align="center">
    <td>-p</td>
    <td>--path</td>
    <td align="left">Path of the image or folder for batch processing</td>
    <td>CWD</td>
    <td>string</td>
  </tr>
  <tr align="center">
    <td>-o</td>
    <td>--out</td>
    <td align="left">Output folder for generated cover arts</td>
    <td>CWD</td>
    <td>string</td>
  </tr>
  <tr align="center">
    <td>-t</td>
    <td>--title</td>
    <td align="left">Cover art's title</td>
    <td></td>
    <td>string</td>
  </tr>
  <tr align="center">
    <td>-sp</td>
    <td>--samepath</td>
    <td align="left">When passing this argument, the output folder is set to the input folder. when using this the --out path should be relative</td>
    <th colspan="2">present or not</th>
  </tr>
  <tr align="center">
    <td>-cli</td>
    <td>--cli</td>
    <td align="left">Run as a CLI without changing default arguments. If no arguments are provided, the program will act in prompt mode. To prevent that, you can use this flag</td>
    <th colspan="2">present or not</th>
  </tr>
  <tr align="center">
    <td>-v</td>
    <td>--version</td>
    <td align="left">Prints version info</td>
    <th colspan="2">present or not</th>
  </tr>
  <tr align="center">
    <td>-h</td>
    <td>--help</td>
    <td align="left">Lists all commands with its description</td>
    <th colspan="2">present or not</th>
  </tr>
</table>

If you want to run this as a CLI without providing or changing default arguments then just run

```sh
coverart -cli
```

</br>

## Development

##### Environment setup

```sh
git clone https://github.com/Tetrax-10/jellyfin-cover-art-generator.git
cd jellyfin-cover-art-generator
pip install pillow termcolor pyreadline3 pyinstaller
```

##### Run

```sh
python cover_art.py <args>
```

##### Build executable

```sh
pyinstaller cover_art.spec
```

Make sure to add your "dist" folder to the PATH so that when you run coveraet, it refers to your "dist" executable. Additionally, also ensure that the path of the installed "coverart.exe" is removed during development.

The installer is compiled with the [Inno Setup Compiler](https://jrsoftware.org/isdl.php), and there's no need to perform this step during the development of Jellyfin Cover Art Generator, as it is only used for distribution

</br>

### Known bugs

1. When this program is installed and uninstalled it leaves this string ";;" in PATH environmental variable, it's not an issue as it doesn't affect the env vars but its a bloat, So please help me fix this as I'm not good with Inno Setup Compiler

</br>

### Assist required

1. Help me to build/test executable for `linux` and `mac os`.
2. Help me fix the `known bugs`.

</br>

### Support

Like This Tool? Gimme Some ❤️ by Liking this Repository.
