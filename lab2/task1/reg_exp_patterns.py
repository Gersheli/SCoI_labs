SENTENCE = r'[.!\?]+'
NON_DECLARATIVE_SENTENCE = r'[!\?]+'
WORD = r'\b[a-zA-Z\d]+\b'
NUMBER = r'\b\d+\b'

SINGLE_WORD_ABBREVIATION = [
    'etc.', 'vs.', 'jr.', 'sr.', 'mr.', 'ms.', 'mrs.', 'smb.', 'smth.', 'adj.', 'prep.', 'pp.', 'par.', 'ex.',
    'pl.', 'edu.', 'appx.', 'sec.', 'gm.', 'cm.', 'yr.', 'jan.', 'feb.', 'mar.', 'apr.', 'jun.', 'jul.', 'aug.',
    'sep.', 'oct.', 'nov.', 'dec.', 'mon.', 'tue.', 'wed.', 'thu', 'fri.', 'sat.', 'sun.',
    ' a.', ' b.', ' c.', ' d.', ' e.', ' f.', ' g.',' j.', ' h.', ' i.', ' g.', ' k.', ' r.', ' l.', ' n.', ' m.',
    ' s.', ' t.', ' o.', ' p.', ' q.', ' w.', ' x.', ' y.', ' z.',
    '.a.', '.b.', '.c.', '.d.', '.e.', '.f.', '.g.','.j.', '.h.', '.i.', '.g.', '.k.', '.r.', '.l.', '.n.', '.m.',
    '.s.', '.t.', '.o.', '.p.', '.q.', '.w.', '.x.', '.y.', '.z.']

TWO_WORD_ABBREVIATIONS = ['e.g.', 'i.e.', 'p.s.', 'ph.d.']
