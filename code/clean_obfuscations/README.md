The python code here is to help automate cleaning of obfuscations in Javascript code generated typically by malicious actors.

## Notes
2024-08-22  
Sample obfuscated code included has 'zzz' in a couple of spots around l256 to prevent someone from running this JS and causing an infection.   They are a part of "my" obfuscation to make this file more safe.  That being said, it's not fully analysed yet, so USE CAUTION when working with this sample JS file. 

## Change Log
- 2024-08-22 - initial version - strips /* ... */  and  // ....

## Bugs
- 2024-08-22 - found to be stripping too much and valid code is being removed (l256)


## Contributors