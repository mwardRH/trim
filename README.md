# Trim
This is a simple application for stripping spaces out of a filename. I strip the spaces out and replace them with perids. The applicaiton supports 1 arugment which is the directory location. 

```bash
python3 trim.py ~/tmp
```

Another option is put the path to the trim.py file in your ~/.bashrc and add a `$(pwd)` at the end. See example below

```bash
alias trim='python3 /run/media/mward/extended/projects/trim/test.py $(pwd)'
```
