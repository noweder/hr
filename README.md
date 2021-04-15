# Building a Command Line Tool with Python

## Description 

A tool that will export a system's user information into formats. The tool will be able to export usernames, IDs, home directories, and shells in either JSON or CSV format. No information about system users themselves will be included in the files. By default, the Python tool will display the information as JSON to stdout, but the `--format` flag will allow a person to specify CSV as an alternative export type. Additionally, if we want the information going to a file instead of stdout, we can specify it by using the `--path` flag.

## Usage

This tool will  export a system's user information into formats that can be used by other departments. The command will be able to export user names, IDs, home directories, and shells as either JSON or CSV. This command will not include information about system users. By default, the command will displaiy the information as JSON to Stdout, but the --format flag will allow a person to specify csv as an alternative export type. Additionally, a file can be specified by using the --path flag. 

Here are the various ways that the tool can be used:
```
$ hr --format=csv --path=path/to/users.csv
$ hr --path=path/to/users.json
$ hr
[
  {
    "name": "cloud_user",
    "id": 1002,
    "home": "/home/cloud_user",
    "shell": "/bin/bash"
  },
  {
    "name": "kevin",
    "id": 1003,
    "home": "/home/kevin",
    "shell": "/bin/zsh"
  },
]
$ hr --format=csv
name,id,home,shell
cloud_user,1002,/home/cloud_user,/bin/bash
kevin,1003,/home/kevin,/bin/zsh
```

## Installation From Source

To install the package after you've cloned the repository, you'll want to run the following command from within the project directory:

```
$ pip install --user -e .
```
