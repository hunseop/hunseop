if (!require("devtools")) install.packages("devtools")
devtools::install_github("ChiHangChen/KeyboardSimulator")
library(KeyboardSimulator)

mouse.move(412,885)
mouse.click("right")
mouse.move(392,729,duration = 0.5)
mouse.click()

Sys.sleep(1)
keybd.press("N+A+V+E+R")
Sys.sleep(0.5)
keybd.press("enter")
Sys.sleep(1)

mouse.move(297,451)
mouse.click()
mouse.move(380,416,duration = 0.5)
mouse.click(,hold = TRUE)

mouse.move(954,414,duration = 0.5)
mouse.release()

keybd.press("ctrl+c")
Sys.sleep(0.5)
keybd.press("win")
Sys.sleep(0.5)
keybd.press("e+x")
Sys.sleep(0.5)
keybd.press("enter")
Sys.sleep(2)
keybd.press("enter")
keybd.press("ctrl+v")


