import subprocess

text = "What do you want me to say?"
language = "en" #try en, en-us, en-sc, en-rp, en-n, en-rp, en-wm, zh (mandarin), el (greek), es (spanish)
genderIdentity = "+f3" #m1 - m7, f1 - f5
# add +croak or +whisper for other effects
# find other variants with command line: espeak --voices=variant
# also check out espeak.sourceforge.net/

print(text)
subprocess.Popen(["espeak", "-v", language+genderIdentity, text])