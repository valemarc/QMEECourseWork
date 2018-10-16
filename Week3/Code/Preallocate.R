a <- NA
for (i in 1:10 ) {
  a = c(a,i)
}
print(a)

a <- rep(NA,10)
for (i in 1:10 ) {
  a[i] = 10
}

print(a)
