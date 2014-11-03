chess_survivability
===================

I was reading [this blog post](http://priorprobability.com/2014/10/22/chess-piece-survival-rates/) and noticed there wasn't any source code provided, so I decided to write a script to do the same analysis. However, after reading the post a bit closer I noticed that the original Quora question did in fact have source code avaiable. So, giving credit where credit is due: http://priorprobability.com/2014/10/22/chess-piece-survival-rates/

The only external library this script requires is python-chess. Install with:

```
pip install python-chess
```

My code (compared to the repo mentioned above) is a bit more concise because a lot of the heavy lifting is done in the python-chess library. It takes in PGN files and prints out the survivability percentage stats. It can also be parallelized to multiple processes (much faster when analyzing multiple files). When analyzing all the player PGN files mentioned [here](http://www.pgnmentor.com/files.html#players) it returned this result:

```
$ ./survivability.py -f *.pgn -p 4
Total games analyzed: 319736
[('e1', '1.000'),
 ('e8', '1.000'),
 ('h2', '0.739'),
 ('h7', '0.719'),
 ('g2', '0.695'),
 ('g7', '0.669'),
 ('a2', '0.635'),
 ('a7', '0.628'),
 ('f2', '0.617'),
 ('f7', '0.606'),
 ('b2', '0.571'),
 ('h1', '0.547'),
 ('h8', '0.536'),
 ('a8', '0.534'),
 ('a1', '0.532'),
 ('b7', '0.531'),
 ('d1', '0.471'),
 ('d8', '0.465'),
 ('e7', '0.400'),
 ('e2', '0.376'),
 ('f1', '0.363'),
 ('c2', '0.357'),
 ('f8', '0.341'),
 ('c8', '0.329'),
 ('c1', '0.317'),
 ('c7', '0.313'),
 ('b8', '0.285'),
 ('d7', '0.279'),
 ('g1', '0.269'),
 ('g8', '0.256'),
 ('b1', '0.255'),
 ('d2', '0.218')]
```

Another exanple:

```
$ ./survivability.py -f Carlsen.pgn Anand.pgn -p 2
Total games analyzed: 4554
[('e1', '1.000'),
 ('e8', '1.000'),
 ('h2', '0.721'),
 ('h7', '0.707'),
 ('g2', '0.677'),
 ('g7', '0.656'),
 ('f2', '0.617'),
 ('f7', '0.599'),
 ('a2', '0.586'),
 ('a7', '0.582'),
 ('b2', '0.539'),
 ('h1', '0.514'),
 ('h8', '0.507'),
 ('a8', '0.501'),
 ('a1', '0.495'),
 ('b7', '0.481'),
 ('d1', '0.435'),
 ('d8', '0.420'),
 ('e7', '0.382'),
 ('c2', '0.354'),
 ('f1', '0.330'),
 ('f8', '0.325'),
 ('e2', '0.324'),
 ('c1', '0.307'),
 ('c8', '0.304'),
 ('d7', '0.275'),
 ('c7', '0.269'),
 ('b8', '0.235'),
 ('g1', '0.235'),
 ('g8', '0.219'),
 ('b1', '0.214'),
 ('d2', '0.198')]
```
