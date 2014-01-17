### Seminar Sorting
### Ethics Day 2014, Kent Denver School

##### Overview

Every year, Kent Denver School hosts a school-wide Ethics Day, on which students discuss ethical issues in their own lives and the world abroad. Students register for a set of student-led seminars, ranking their first five choices. This software aims to sort students into seminars. 

##### Algorithm

We optimize two things: student seminar choices and age distribution (having equal numbers of freshman, sophomores, juniors, and seniors in each seminar). Students are assigned to the highest-ranked seminar with an open seat. In order to also optimize age distribution, however, we run a [Monte Carlo simulation](http://en.wikipedia.org/wiki/Monte_Carlo_method), randomly sampling the order in which students are assigned. We then choose the ordering of students which, when assigned, creates seminars with the best age distribution. 