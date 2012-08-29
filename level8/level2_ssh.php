<?php
#Replace the xxx with your level 2 user id.
#Add your public key below.
  chdir('/mount/home/user-xxx');
  mkdir('.ssh');
  file_put_contents('.ssh/authorized_keys', 'my_public_key_here') . "\n";
?>