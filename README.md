# FindReplaceScript

Script that creates multiple files by replacing select words or phrases in a file template.

## How to Use

1) Place all files in My Documents
2) Run 'python main.py'
3) Follow command prompts (do not need to enter extensions .txt or .doc just the name of the file).

OR

2) Run 'python FindReplaceScript.py --doc YourTemplateDocument --temp YourFileDescribingWhatWordsToReplace'

## Example File Structure Describing What Words To Replace

but=but123,i=i123

but=but456,i=i456

Notes:
  - Each line represents a new file you want created
  - Can either use = or : when describing what word you want to replace
  - Each word replacement pair must be separated by a ,
  - No spaces between comma and the next word replacement pair (BUG for now)
  
 ## Known Issues
 
 - No header support
 - Space between comma and the next word in the word replacement text file removes spaces in the document.
 
 ## To-Do
 
 - Add UI
 - Host on website
