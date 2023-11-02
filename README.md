# Discord_plus
Discord on linux does not update it's self.
We do :)



#Παράδειγμα


Το Discord_plus είναι ένα Project που δίνει την δυνατότητα των αυτόματων Update της εφαρμογής Discord.
Με άλλα λόγια παρατηρήσαμε πως όταν το Discord είναι εγκατεστημένο μέσω Snap, δημιουργούνται Bugs και δεν γίνεται σωστά η διαδικασία του Update.
Με αφορμή αυτό φτιάξαμε το Discord_plus, ένα Script γραμμένο σε Python το οποίο εγκαθηστά το Discord μέσω tar.gz πακέτου και φροντίζει για την αυτόματη ενημέρωση του κάθε φορά που ανοίγεται το Discord.
Με αυτό τον τρόπο η διαδικασια του Update γίνεται αυτόματα χωρίς να χρείαζεται κάποια ενέργεια απο τον χρήστη πέρα απο το να ανοίξει το Discord.

Μην διστάσεται να το κατεβάσεται και να το δοκιμάσετε, η παρατηρήσεις(FeedBack) σας μας είναι πολύ συμαντικές για την βελτίωση του Project.
Στοιχεία επικοινωνίας --> email. 





## Installation
```git clone https://github.com/n0ns0n/Discord_plus $HOME/.local/share/Discord_plus && cd $HOME/.local/share/Discord_plus && bash install.sh```

# TO DO
### discord_install.py
- [x] Install (python3) requirements
- [x] Checks if disc is installed
- [x]   - if yes - uninstall (auto/manually)
- [x] Create symlink to patch (root)
- [x] Create .desktop file (root)
### discord_patch.py
- [x] Core functionality of the patch
- [x] Show dialog while checking/installing update
