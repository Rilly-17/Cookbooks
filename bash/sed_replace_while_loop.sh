find .  -name main.tf | while read main ; do sed -i 's/1.21/1.56.0/g' $main ; done

# uses find command to find all files named main.tf in current and child folders, then pipes that output to the while command, which replaces the version number with sed on each file
