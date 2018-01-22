# -*- coding: utf-8 -*-
import os
import sys
import time
import subprocess

# 相对路径
PY_SCRIPT_DIR="scripts"
TMP_LOG_DIR="tmp_log_dir"
def do(script_name):
    log_path_str = os.path.join(PY_SCRIPT_DIR, TMP_LOG_DIR, script_name +".log")
    DO_PY_COMMAND = "python " + os.path.join(PY_SCRIPT_DIR, script_name) + "> " + log_path_str )
    subprocess.Popen(DO_PY_COMMAND,stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True)

    # f_stream = os.popen(DO_PY_COMMAND, DO_PY_COMMAND_MODLE)
    f_stream = subprocess.Popen(DO_PY_COMMAND,stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True)
    while f_stream.poll()==None:
        sys.stdout.flush()
        stdout_readline = f_stream.stdout.readline()
        # print type(stdout_readline)
        sys.stdout.write(stdout_readline)

        stderr_readline = f_stream.stderr.readline()
        # if stderr_readline :
        sys.stdout.write(stderr_readline)

    return f_stream.returncode

if __name__ == "__main__":
    print  do("do_miccn_logon.py"), "  <<<<<"
  