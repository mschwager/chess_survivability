#!/usr/bin/env python

import pprint
import argparse
import collections
import multiprocessing

import chess
import chess.pgn

def analyze_pgn(filename):
    result = collections.Counter()

    for game in games(open(filename)):
        pieces = range(16) + ([None] * 32) + range(48, 64)
        for variation in variations(game):
            to = variation.move.to_square
            fr = variation.move.from_square
            pieces[to], pieces[fr] = pieces[fr], None

            # Handle castling. This is the only situation where two pieces
            # move at once. Need to check that the King is the one moving
            # as well, since other pieces can e1 -> g1, e8 -> g8, etc.
            is_king = lambda i: str(variation.board().piece_at(i)).upper() == 'K'
            if str(variation.move) == 'e1g1' and is_king(to):
                pieces[5], pieces[7] = pieces[7], None
            if str(variation.move) == 'e8g8' and is_king(to):
                pieces[61], pieces[63] = pieces[63], None
            if str(variation.move) == 'e1c1' and is_king(to):
                pieces[3], pieces[0] = pieces[0], None
            if str(variation.move) == 'e8c8' and is_king(to):
                pieces[59], pieces[56] = pieces[56], None

        result.update({i: 1 for i in pieces if i is not None})

    return result

def games(fd):
    game = chess.pgn.read_game(fd)
    while game:
        yield game
        game = chess.pgn.read_game(fd)

def variations(game):
    var = game.variations
    while var:
        yield var[0]
        var = var[0].variations

def parse_args():
    p = argparse.ArgumentParser(description=
        '''
        Print the survivability of chess pieces based on their starting
        locations.
        ''', formatter_class=argparse.RawTextHelpFormatter)

    p.add_argument('-f', '--pgn-files', nargs='+', required=True)
    p.add_argument('-p', '--parallelization', default=1, type=int)

    args = p.parse_args()
    return args

def main():
    args = parse_args()

    result = collections.Counter()
    pool = multiprocessing.Pool(processes=args.parallelization)
    result_list = pool.map(analyze_pgn, args.pgn_files)
    
    for r in result_list:
        result.update(r)

    # The King always "survives" so the number of times we've seen him "survive"
    # is the number of games analyzed. His starting location is e1 (4 in the
    # board list).
    game_count = result[4]

    print "Total games analyzed: {}".format(game_count)
    percentages = {chess.SQUARE_NAMES[k]: "{:.3f}".format(float(v) / float(game_count))
        for k, v in result.iteritems()}
    pprint.pprint(sorted(percentages.items(), key=lambda x: x[1], reverse=True))

if __name__ == "__main__":
    main()
