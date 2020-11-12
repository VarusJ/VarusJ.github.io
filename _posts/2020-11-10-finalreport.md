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
最后一个阶段是要求我们完成三个扩展任务：ImageProcessing，MazeBug，N-Puzzle，这部分我在 vmatrix 上的 readme 中有详细介绍，这里只展示成果和简要说明（puzzle 无可视结果展示）：

<center>
  <img src="https://github.com/VarusJ/VarusJ.github.io/raw/master/_posts/finalreport-img/imgreader.png" alt="circlebug" width="45%"/>    
  <img src="https://github.com/VarusJ/VarusJ.github.io/raw/master/_posts/finalreport-img/maze.png" alt="spiralbug" width="45%"/>   
</center>
- ImageReader:
    ImplementImageIO
    实现IImageIO的myRead接口
    使用二进制读取图片文件的方式，解析读到的位图文件的位图头、位图信息。主要是对读到的位图信息的一个解析，要将每四个字节代表的数字转成Java数字变量，以进行后面的运算和判断。转化的方法就是对这四个字节代表的数字赋予不同的位权，也就是移位，有了位权之后再将四个字节组合起来看就可以得到这四个字节代表的数字。另外一个重点是，RGB像素的理解。这里用的是24位彩图，每个像素是3个字节，分别对应红绿蓝三种颜色。除了24位图还有的就是，1位（八个像素一个字节），4位（两个像素一个字节），8位（一个像素一个字节），这三种都需要用调色板来对自己表示的颜色进行编号，24位则不用。需要注意的是，Java里面的Image是需要每个像素四个字节的，其中第四个字节是指图片的透明度。因为保存到图片文件里面的时候是不记录透明度的，所以在用从文件里读取和解析出来的RGB像素信息构造Java的Image时需要对每个像素再加一个字节，代表透明度（默认不透明）。
    实现IImageIO的myWrite接口（使用ImageIO.write()）
    ImplementImageProcessor
    实现IImageProcessor的四个色彩通道筛选接口，红绿蓝三种色彩通道的实现方法是类似的，都可以通过只提取RGB三色中对应的一种颜色来完成颜色筛选，而灰色稍有不同，灰色的RGB需要由计算得出，因此用到一条灰度公式 I = 0.299 R + 0.587 G + 0.114 * B。通过这条公式可以将原来的彩色图像的RGB转化为灰色图像的RGB，这条公式的大致原理就是使RGB三色的值大致趋同，三色对应的RGB值越接近，就越接近灰色。

- Maze Bug: 
    深度优先搜索算法的基本思想。是沿着树的深度遍历树的节点，尽可能深地搜索树的分支，换句话说就是一条路走到黑。深度优先算法将不停地一直搜索，直至搜索到想要的节点或者所有节点都已被访问过（即没搜到）。所以将深度优先算法应用于走迷宫是个很合适的选择，前提是要解的迷宫是无环的，否则会导致深度优先算法无法遍历所有节点，可能会出现节点存在但搜不到的情况。
    深度优先搜索算法的基本步骤。
    先将树的所有节点标记为”未访问”状态。
    输出起始节点，将起始节点标记为”已访问”状态。
    将起始节点入栈。
    当栈非空时重复执行以下步骤：
    取当前栈顶节点。
    如果当前栈顶节点是结束节点（迷宫出口），输出该节点，结束搜索。
    如果当前栈顶节点存在”未访问”状态的邻接节点，则选择一个未访问节点，置为”已访问”状态，并将它入栈，继续步骤1。
    如果当前栈顶节点不存在”未访问”状态的邻接节点，则将栈顶节点出栈，继续步骤1。
    进阶—方向概率选择
    原理。五个评估成绩的迷宫都有一定的方向偏向性，如图四就有向上和向左的偏向性。在行走正确路径时，对四个方向的选择次数进行统计，从而控制随机选择时选择某个方向的概率。增加方向的概率估计后能有效地提高走迷宫的效率。
    方向次数数组的维护。四个方向选择次数默认都是1，如果第一个节点选择向左，则向左次数加1，同理，其他方向和其他节点，选什么方向就什么方向次数加1。而减少的时候是在搜索到一条死路准备回退时，回退的时候要注意的是，每回退一格，就要将该回退方向的反方向的次数减1（一不注意可能忘记取反方向了）。



- N-puzzle:
基本思想是采用 bfs：将起始节点放入一个open队列中    
如果open队列为空，则搜索失败，问题无解；否则重复以下步骤：  
访问open队列中的第一个节点v，若v为目标节点，则搜索成功，退出。  
从open队列中删除节点v，放入close集合中。  
将所有与v邻接且未曾被访问的节点放入open队列中。
问题的发现。在运行main测试样例的时候，发现总是要卡个近十秒才出结果。虽然后面结果出来的时候总是显示运行平均时间才50来毫秒，但是一想这似乎不匹配啊，然后仔细看了main函数的测试方法后才发现原来真正耗时的是前面的bfs，显示的平均运行时间仅仅是A*算法的时间。这样一来，转念一想就知道bfs的查询部分是最耗时的了，每步广度优先搜索都有一个要判断是否在当前查询节点是否在队列中的操作，而队列是个线性表，广搜涉及的节点非常之多，所以在一个超长队列里进行查询是非常不妥的。因此用来查询的应该必须是像close那样，是一个集合，集合的查询是非常快的，尤其是哈希集合。我的close一开始就是用的哈希集合，所以自然而然地想到了这一点。
问题的解决。因为集合里的元素是无序的，所以集合没有像队列一样的操作，然而广搜是需要通过队列来实现的，所以一个折中的方案就是，仅仅查询的时候是用集合来查询，算法的正常运作还是得靠队列来维护。因此我新建了一个和open队列保持一样元素的哈希集合，这个集合在队列add的时候同时add，remove的时候同时remove，始终保持一致。集合的作用就仅仅是用来执行查询。虽然听起来有点浪费空间，但这在时间上快得还真不止一点点，和之前的运行时间完全不是一个量级，所以我认为这点空间冗余完全是值得的，改进之后的bfs，几乎都是秒出结果。
估价函数：主要作用是用来估计节点n的重要性，表示为：从起始节点，经过节点n，到达目标节点的代价。代价越小，节点就越优良，在搜索的时候就应该更优先搜索，这就是所谓的启发式搜索。我的估价函数主要是用了三个评估方法，分别是：后续节点不正确的个数。当前位置的节点后面的节点不是本来应该在其后面的节点。将有这种情况的节点都记个数统计起来，某种意义上当成是一种代价。
曼哈顿距离。曼哈顿距离通俗地说其实就是折线距离。计算当前节点所在位置到其本来应该在的位置的曼哈顿距离，充当一种代价。
欧几里得距离。欧几里得距离是平常所说的直线距离。计算当前节点所在位置到其本来应该在的位置的欧几里得距离，充当一种代价。
权值。既然三种评估方法都各有其代价，而且代价的衡量尺度也无法从某种意义上找到联系。就只能人为地给每种评估方式的代价加上一个权重，代表该种评估方法的重要性，以实现将这三种不相关的估计方式联系起来。权重的参数是需要慢慢调整的，所以真正花时间的是调参。   

- **总结（stage4）**   
这就是大三上学期经历的整个中级实训的报告了，这也是整个实训的最后一个总结阶段。这次实训最大的收获就是锻炼了强大的快速学习的能力，由于之前有接触过 Java 所以这方面其实对我算是一种巩固和复习，除此之外，还有 Ant、Junit、Sonar 等集成编译、运行、测试和代码规范检查的黑科技。总的来说，工作量很大，很具有挑战，同时我的收获也很多。终于结束了本次的中级实训，比起上一次初级实训的体会更加丰富和深刻。





