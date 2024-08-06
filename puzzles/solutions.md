## CYBER PUZZLES: THE SOLUTIONS
### [🏡 ErnieJohnson.ca - Portfolio Web Site](https://www.erniejohnson.ca)

<a href="mailto:ej8899@gmail.com" target="_blank"><img src="https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white" alt="send email to ej8899@gmail.com" /></a>&nbsp;<a href="https://www.linkedin.com/in/ernie-johnson/" target="_blank"><img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="linkedin" /></a>&nbsp;<a href="https://flowcv.com/resume/0chloacpte"><img alt="Static Badge" src="https://img.shields.io/badge/RESUME-8A2BE2?style=for-the-badge"></a>
---

Developing investigative skills is crucial for excelling in cybersecurity as it enables us professionals to identify, analyze, and mitigate threats effectively. These skills will help you in understanding attack vectors, tracing the origin of breaches, and uncovering the methods used by cybercriminals.

By honing investigative techniques, cybersecurity experts can respond swiftly to incidents, minimize damage, and enhance the overall security posture of their organizations. Moreover, strong investigative abilities facilitate continuous learning and adaptation, which are essential in the ever-evolving landscape of cyber threats.

In other words - don't cheat - follow the steps and learn, or develop your own flow of solving the problems!  Document as you go!

---
[click for the PUZZLES](README.md)  

<details>
<summary><BIG><b>emoji image steps to a solution (click)</b></big></summary>  

- downloaded the image  

- opened it then looked for EXIF data (nothing obvious)  

- did a google search for exif viewers in case I missed something in the above - found this one: https://jimpl.com/

- Looked at that, found 'suspect' information (it says there is 39 bytes in meta data - not sure that's were the message was though

- opened it in a hex editor ( https://hexed.it/ ) to have a closer look.  Nothing too significant to find there, so I assumed it was embedded into the image pixels themselves.

- that takes us on to  steganography. I did a google search and this was the first in my google search: https://stylesuxx.github.io/steganography/  - you'll find the answer in there.
</details>

<details>
<summary><BIG><b>secrets.txt (click)</b></big></summary> 

- downloaded the file  

- opened it in my favorite text editor (Sublime Text 4)

- observed hex data only - no  obvious text was present


- looked up file signatures (magic numbers) and compared the first few bytes.  Newbies - you'll want to remember that the first few bytes of a file are the magic number.  You can find a list of these here: https://en.wikipedia.org/wiki/List_of_file_signatures
and here: https://www.garykessler.net/library/file_sigs.html

- recognize it a GZIP file.

- let gzip undo it's thing to reveal the message
</details>
---
<div align="right"><img src="https://komarev.com/ghpvc/?username=ej8899-cyber-projects&style=flat-square&color=008080" alt=""/></div>