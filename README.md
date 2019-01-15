# GG - Gibberish Generator

Gibberish Generator that uses a bigram maximum likelihood estimate. It predicts the most appropriate word based on the previous word.

Probabilities are calculated based on the text in 'text.txt' file.

## Usage

Replace text in 'text.txt' with arbitrary text. The longer it is, the longer it will take for probabilities to calculate.

Run 'main.py'. Currently the script includes a simple example that generates 10 sentences.

## Note

Probabilites calculation is not very efficient, so it may take a while to calculate if 'text.txt' includes long text!
