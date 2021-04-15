# Building a Command Line Tool with Python

## The Scenario
We've been asked to create a tool that will export a system's user information into formats that various other departments can use. The tool will be able to export usernames, IDs, home directories, and shells in either JSON or CSV format. No information about system users themselves will be included in the files. By default, the Python tool will display the information as JSON to stdout, but the `--format` flag will allow a person to specify CSV as an alternative export type. Additionally, if we want the information going to a file instead of stdout, we can specify it by using the `--path` flag.

## Usage
....

## Installation From Source

To install the package after you've cloned the repository, you'll want to run the following command from within the project directory:

```
$ pip install --user -e .
```
