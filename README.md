# PSN-discount-scrapper

PSN-discount-scrapper is a simple program to scrap (collect) and sort all discount games within a threshold in Playstation store.

For more detail, please check out my output file in `example` folder

## Instructions

1.&nbsp;First download the folder (or the `scrapper_app`)

2.&nbsp;Open up your terminal (MacOS/Linux) and access the downloaded folder.

3.&nbsp;Simply run the app by run this command in your terminal:

```bash
./scrapper_app
```

4.&nbsp;Wait for about 10 mins (may vary based on your connection speed) until the program is exited

5.&nbsp;The output will be written in `discount_game_list.txt`

## [Dev] Installation

Create python's virtual environment, then activate it

```bash
virtualenv .env
source .env/bin/activate
```

Install requirements

```bash
pip3 install -r requirements.txt
```

Run the program

```bash
python3 app.py
```

## Disclaimer

This is just a tool to help people (personally me) to find discount games easier in Playstation store.
