---
title: 'Final Report'
date: 2020-11-10
permalink: /posts/2020/11/finalreport/
tags:
  - personal
  - course
---

# Final Report 
## 18342040 景致

This blog is a course report for Gridworld.

**A review**  

整体来回顾一下实训的全部过程。   
10 月 10 号开始了我们的实训，本次实训分为了四个阶段。  

- **Stage1**  
本次实训第一阶段自学了 Vi/Vim, Java, Ant, Junit 的相关知识。首先认识并熟悉 Vi/Vim 的三种开发模式和基本使用方法，之后我们认识并熟悉了 Java 的使用，并要求实现 helloworld 和图形计算器，掌握利用 Ant 编译和运行项目的方法，最后是学会利用 Junit 实现对类方法的测试。这一部分的自学报告也在此目录下。  
另外就是为之后的大项目进行一些预备工作 (part1)，这里是要求我们跑通 bug runner 的 demo，同时学会使用 sonar runner 来对代码风格进行检查。同时，我们需要基于对 bug runner 的观察回答一系列问题。

- **Stage2**  
这个阶段的任务是完成有这若干功能的 bug 的实现，同时还要基于源代码的阅读和实验的观察回答一系列相关的问题。这个阶段一共分为了 4 个 part，每个 part 有对应的要求。  
    + part2  
    这一部分，我们需要完成：  
      1. CircleBug: identical to BoxBug, except that in the act method the turn method is called once instead of twice
      2. SpiralBug: drops flowers in a spiral pattern. Hint: Imitate BoxBug, but adjust the side length when the bug turns
      3. ZBug: move in a “Z” pattern, starting in the top left corner. After completing one “Z” pattern, a ZBug should stop moving.
      4. DancingBug: “dances” by making different turns before each move. 

    以下是我完成的截图和gif: 
    <center>
      <img src="https://github.com/VarusJ/VarusJ.github.io/raw/master/_posts/finalreport-img/circlebug.gif" alt="circlebug" width="45%"/>    
      <img src="https://github.com/VarusJ/VarusJ.github.io/raw/master/_posts/finalreport-img/spiralbug.gif" alt="spiralbug" width="45%"/>   
      <img src="https://github.com/VarusJ/VarusJ.github.io/raw/master/_posts/finalreport-img/dancingbug.gif" alt="dancingbug" width="45%"/> 
      <img src="https://github.com/VarusJ/VarusJ.github.io/raw/master/_posts/finalreport-img/zbug.gif" alt="zbug" width="45%"/> 
    </center>
   
    + part3  
    这一部分，我们需要完成：  
      1. Jumper: can move forward two cells in each move. It “jumps” over rocks and flowers. It does not leave anything behind it when it jumps.

    以下是我完成的截图和gif: 
    <center>
      <img src="https://github.com/VarusJ/VarusJ.github.io/raw/master/_posts/finalreport-img/jumper.gif" alt="jumper" width="45%"/> 
      <img src="https://github.com/VarusJ/VarusJ.github.io/raw/master/_posts/finalreport-img/jumpertest.png" alt="jumpertest" width="45%"/>    
    </center>

    + part4  
    这一部分，我们需要完成：  
      1.  ChameleonKid: that extends ChameleonCritter as modified in exercise 1. A ChameleonKid changes its color to the color of one of the actors immediately in front or behind. If there is no actor in either of these locations, then the ChameleonKid darkens like the modified ChameleonCritter.
      2. RockHound: that extends Critter. A RockHound gets the actors to be processed in the same way as a Critter. It removes any rocks in that list from the grid. A RockHound moves like a Critter.
      3. BlusterCritter that extends Critter. A BlusterCritter looks at all of the neighbors within two steps of its current location. 
      4. QuickCrab: that extends CrabCritter. A QuickCrab processes actors the same way a CrabCritter does. A QuickCrab moves to one of the two locations, randomly selected, that are two spaces to its right or left, if that location and the intervening location are both empty. Otherwise, a QuickCrab moves like a CrabCritter.
      5. KingCrab: that extends CrabCritter. A KingCrab gets the actors to be processed in the same way a CrabCritter does. A KingCrab causes each actor that it processes to move one location further away from the KingCrab. If the actor cannot move away, the KingCrab removes it from the grid. When the KingCrab has completed processing the actors, it moves like a CrabCritter.


    以下是我完成的截图和gif: 
    <center>
      <img src="https://github.com/VarusJ/VarusJ.github.io/raw/master/_posts/finalreport-img/bluster.gif" alt="circlebug" width="45%"/>    
      <img src="https://github.com/VarusJ/VarusJ.github.io/raw/master/_posts/finalreport-img/chameleon.gif" alt="spiralbug" width="45%"/>   
      <img src="https://github.com/VarusJ/VarusJ.github.io/raw/master/_posts/finalreport-img/king.gif" alt="dancingbug" width="45%"/> 
      <img src="https://github.com/VarusJ/VarusJ.github.io/raw/master/_posts/finalreport-img/quick.gif" alt="zbug" width="45%"/> 
      <img src="https://github.com/VarusJ/VarusJ.github.io/raw/master/_posts/finalreport-img/rockhound.gif" alt="zbug" width="45%"/> 
    </center>






