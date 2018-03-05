"""
NAME:               Mortal Fibonacci Rabbits (Bioinformatics Stronghold)
CONTRIBUTOR:        Aakash Sudhakar

PROBLEM:            Recall the definition of the Fibonacci numbers from 
                    “Rabbits and Recurrence Relations”, which followed the 
                    recurrence relation F_{n} = F_{n-1} + F_{n-2} and 
                    assumed that each pair of rabbits reaches maturity in one month 
                    and produces a single pair of offspring (one male, one female) 
                    each subsequent month.

                    Our aim is to somehow modify this recurrence relation to achieve 
                    a dynamic programming solution in the case that all rabbits die out 
                    after a fixed number of months.

DATASET:            Positive integers n ≤ 100 and m ≤ 20.

OUTPUT:             The total number of pairs of rabbits that will remain after 
                    the n-th month if all rabbits live for m months.

SAMPLE DATASET:     6 3
SAMPLE OUTPUT:      4

STATUS:             Pending.
"""

def main():
    # NOTE: Requires being in parent repo ('pwd' must return up to directory '/Rosalind_Bioinformatics/Bioinformatics_Stronghold')
    # FILEPATHREAD = "./datasets/P11_FIBD-dataset.txt"
    FILEPATHREAD = "./datasets/P11-sample.txt"
    FILEPATHWRITE = "./outputs/P11_FIBD-output.txt"

    # Reads text data from raw dataset as single-line array of characters
    with open(FILEPATHREAD, "r") as fr:
        data = fr.read()

    # Creates output file and writes appropriate response to file and notifies user
    # with open(FILEPATHWRITE, "w") as fw:
    #     fw.write()

    return print("\nThe Mortal Fibonacci dataset has been processed and the appropriate output has been saved to {}.\n".format(FILEPATHWRITE))