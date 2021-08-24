while [ true ]
do
  dd if=/dev/zero of=/Users/<homefolder>/Desktop/junk bs=1024 count=5120000
  rm -f /Users/<homefolder>/Desktop/junk
done