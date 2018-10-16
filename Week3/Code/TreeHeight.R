# This loop calculates heights of trees found in the trees.csv file based on the 
# given distance of each tree from its base
# and angle to its top, using  the trigonometric formula 
#
# height = distance * tan(radians)
#
# OUTPUT
# The heights of the tree, same units as "distance"

MyData <- read.csv("../data/trees.csv")

for(i in MyData) {
  species <- MyData$Species
  degrees <- MyData$Angle.degrees
  distance <- MyData$Distance.m
  radians <- degrees * pi / 180
  height <- distance * tan(radians)
  #print(paste("Tree height is:", height))
  #dfrm <- data.frame(Species = species, Distance.m = distance, Angle.degrees = degrees, Tree.height.m = height)
  write.csv(data.frame(Species = species, Distance.m = distance, Angle.degrees = degrees, Tree.height.m = height),file="../results/TreeHts.csv", append=TRUE)
}



