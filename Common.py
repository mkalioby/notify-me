__author__ = 'mohamed'
import subprocess


def run(excuter, Wait=True, ignore_stderr=False):
    PIPE = subprocess.PIPE
    p = subprocess.Popen(excuter,stdout=PIPE, stderr=PIPE, shell=True)
    out = ""
    err = ""
    if Wait:
        while p.poll() is None:
            err += "".join(p.stderr.readlines())
            out += "".join(p.stdout.readlines())
        return [p.returncode, err , out]
    return p
