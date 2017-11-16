\ Model course_schedule
\ LP format - for model browsing. Use MPS format to capture full model detail.
Maximize
  10 x_作業研究 + 10 x_軟體工程導論
   + x_微算機原理與應用（含實驗） + 5 x_軟體設計
   + 8 x_python研讀 + 10 x_情緒與壓力管理
   + 10 x_空間資料分析專論 + 8 x_Javascript讀書會
   + 2 x_環境,職業與健康人生
Subject To
 R0: 3 x_作業研究 + 3 x_軟體工程導論
   + 4 x_微算機原理與應用（含實驗） + 3 x_軟體設計
   + 2 x_情緒與壓力管理 + 3 x_空間資料分析專論
   + 2 x_環境,職業與健康人生 <= 15
 R1: 9 x_作業研究 + 9 x_軟體工程導論
   + 48 x_微算機原理與應用（含實驗） + 7 x_軟體設計
   + 3 x_python研讀 + x_情緒與壓力管理
   + 4 x_空間資料分析專論 + 4 x_Javascript讀書會
   + x_環境,職業與健康人生 <= 40
 R2: x_情緒與壓力管理 <= 5
 R3: 2 x_軟體工程導論 <= 5
 R4: 3 x_軟體設計 + 3 x_環境,職業與健康人生 <= 5
 R5: 4 x_微算機原理與應用（含實驗）
   + 4 x_空間資料分析專論 <= 5
 R6: 5 x_作業研究 <= 5
 R7: <= 5
Bounds
Binaries
 x_作業研究 x_軟體工程導論
 x_微算機原理與應用（含實驗） x_軟體設計 x_python研讀
 x_情緒與壓力管理 x_空間資料分析專論 x_Javascript讀書會
 x_環境,職業與健康人生
End
