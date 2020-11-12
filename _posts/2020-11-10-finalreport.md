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

    + part5
    这一部分我们需要做做一个 sparse bounded grid, unbounded grid，这个在之前演示中可以很轻松观察到。另外，本次实验还要求我们用 HashMap 或 TreeMap 改写 SparseBoundedGrid，代码如下：
    ```java
      package info.gridworld.withs3.grid;

      import java.util.ArrayList;

      public class SparseBoundedGrid<E> extends AbstractGrid<E> {

          private final SparseGridNode[] occupantArray;
          private final int numCols;
          private final int numRows;

          /**
          * @Author varus
          * @Description SparseBoundedGrid - constructor with the given dimensions
          * @Date 9:11 上午 2020/10/20
          * @Param [rows, cols - number of rows and columns in BoundedGrid]
          */
          public SparseBoundedGrid(int rows, int cols) {
              if (rows <= 0)
                  throw new IllegalArgumentException("rows <= 0");
              if (cols <= 0)
                  throw new IllegalArgumentException("cols <= 0");
              numCols = cols;
              numRows = rows;
              occupantArray = new SparseGridNode[rows];
          }

          /**
          * @return row number
          * @Author varus
          * @Description getNumRows - getter
          * @Date 9:11 上午 2020/10/20
          * @Param []
          */
          public int getNumRows() {
              return numRows;
          }

          /**
          * @return column number
          * @Author varus
          * @Description getNumCols - getter
          * @Date 9:12 上午 2020/10/20
          * @Param []
          */
          public int getNumCols() {
              return numCols;
          }

          /**
          * @return validity
          * @Author varus
          * @Description isValid - tests the validity of a location
          * @Date 9:12 上午 2020/10/20
          * @Param [loc]
          */
          public boolean isValid(Location loc) {
              return 0 <= loc.getRow() && loc.getRow() < getNumRows() && 0 <= loc.getCol()
                      && loc.getCol() < getNumCols();
          }

          /**
          * @return an array list of occupied locations
          * @Author varus
          * @Description getOccupiedLocations - gets the occupied locations
          * @Date 9:13 上午 2020/10/20
          * @Param []
          */
          public ArrayList<Location> getOccupiedLocations() {
              ArrayList<Location> theLocations = new ArrayList<Location>();
              // checking all locations.
              for (int r = 0; r < getNumRows(); r++) {
                  SparseGridNode p = occupantArray[r];
                  while (p != null)
                  {
                      Location loc = new Location(r, p.getColumn());
                      theLocations.add(loc);
                      p = p.getNext();
                  }
              }
              return theLocations;
          }

          /**
          * @return the object at loc
          * @Author varus
          * @Description get - gets the object at loc
          * @Date 9:13 上午 2020/10/20
          * @Param [loc]
          */
          public E get(Location loc) {
              if (!isValid(loc))
                  throw new IllegalArgumentException("Location " + loc + " is not valid");
              SparseGridNode p = occupantArray[loc.getRow()];
              while (p != null)
              {
                  if (loc.getCol() == p.getColumn())
                      return (E) p.getOccupant();
                  p = p.getNext();
              }
              return null;
          }

          /**
          * @return the object put
          * @Author varus
          * @Description put - puts an object at loc
          * @Date 9:16 上午 2020/10/20
          * @Param [loc, obj]
          */
          public E put(Location loc, E obj) {
              if (!isValid(loc))
                  throw new IllegalArgumentException("Location " + loc + " is not valid");
              if (obj == null)
                  throw new NullPointerException("obj == null");
              E oldOccupant = remove(loc);
              SparseGridNode p = occupantArray[loc.getRow()];
              occupantArray[loc.getRow()] = new SparseGridNode(obj,
                      loc.getCol(), p);
              return oldOccupant;
          }

          /**
          * @return the object removed
          * @Author varus
          * @Description remove - removes the object at loc
          * @Date 9:17 上午 2020/10/20
          * @Param [loc]
          */
          public E remove(Location loc) {
              // first check, then search and remove
              if (!isValid(loc))
                  throw new IllegalArgumentException("Location " + loc
                          + " is not valid");
              E obj = get(loc);
              if (obj == null) return null;
              SparseGridNode p = occupantArray[loc.getRow()];
              if (p != null) {
                  if (p.getColumn() == loc.getCol())
                      occupantArray[loc.getRow()] = p.getNext();
                  else {
                      SparseGridNode q = p.getNext();
                      while (q != null && q.getColumn() != loc.getCol()) {
                          p = p.getNext();
                          q = q.getNext();
                      }
                      if (q != null)
                          p.setNext(q.getNext());
                  }
              }
              return obj;
          }
      }
    ```
- **Stage3**   
最后一个阶段是要求我们完成三个扩展任务：ImageProcessing，MazeBug，N-Puzzle，这部分我在 vmatrix 上的 readme 中有详细介绍，这里只展示成果（puzzle 无可视结果展示）：

<center>
  <img src="https://github.com/VarusJ/VarusJ.github.io/raw/master/_posts/finalreport-img/imgreader.png" alt="circlebug" width="45%"/>    
  <img src="https://github.com/VarusJ/VarusJ.github.io/raw/master/_posts/finalreport-img/maze.png" alt="spiralbug" width="45%"/>   
</center>


这就是大三上学期经历的整个中级实训的报告了。总的来说，工作量很大，很具有挑战，同时我的收获也很多。





