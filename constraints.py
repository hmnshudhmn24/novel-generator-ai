# A playful ~256-char core that can “novelize” a seed string by
# repeating/warping it into chapters with simple mutations.
# (Readable version below; strip whitespace/comments to ~256 chars easily.)

def micro_novel(seed: str, words: int = 1000) -> str:
    import random, re
    z=seed.split()
    out=[]
    while len(out)<words:
        w=random.choice(z)
        # mutate: stutter, rhyme-ish suffix, mirror, uppercase shout
        r=random.random()
        if r<.15: w=w+w[:max(1,len(w)//3)]
        elif r<.3: w=w+random.choice(["-ish","-like","-esque","…"])
        elif r<.45: w=w[::-1]
        elif r<.6: w=w.upper()
        out.append(w)
        if random.random()<.08: out.append("\n\n")  # paragraph break
    # basic spacing
    txt=" ".join(out)
    txt=txt.replace(" \n\n ","\n\n")
    txt=re.sub(r"\s+([,.;:?!])",r"\1",txt)
    return txt
