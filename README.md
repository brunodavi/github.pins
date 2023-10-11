# github.pins
Get the names of pinned repositories from GitHub without needing authentication.


## Development
Tips of basic use this project


### Install Dependencies
`pip install -r requirements.txt`


### Export Data
`scrapy runspider main.py -O repos.csv -O repos.json`


`repos.csv`
```csv
reposName
my-project
.dotfiles
```

`repos.json`
```json
[
{"repoName": "my-project"},
{"repoName": ".dotfiles"}
]
```