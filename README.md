# 🚀 Day 41: Set Matrix Zeroes
## Challenge:
Given a 2D matrix mat[][] of size n × m, modify the matrix such that if mat[i][j] == 0, then the entire i-th row and j-th column should be set to 0.
Do this in-place (i.e., without using extra space).

## 📥 Input:
- A 2D matrix mat[][] with n rows and m columns.

## 📤 Output:
- The same matrix, updated such that all rows and columns containing any 0 are set to 0.

## 🧠 Approach
1. First row & first column check karo
Dekhna hai kahin first row ya column mein already 0 hai kya.

2. Baaki matrix ko traverse karo
Agar kisi bhi mat[i][j] pe 0 mila, toh us row aur column ka first element 0 mark karo.

3. Matrix ko update karo using marks
Pehle mark kiya hua data use karke baaki matrix mein 0 lagao.

4. First row & column ko end mein update karo
Kyunki ye log flags ki tarah use hue hain, unhe baad mein process karna hoga.

## ⏱ Time Complexity:
- O(n × m) — Har element ek baar visit hota hai.

## 📦 Space Complexity:
- O(1) — No extra space used, only matrix ke andar hi sab kaam.

## 📚 Reflection:
Yeh problem dikhne mein simple lagti hai but constant space condition usse tricky bana deti hai. Smartly first row/col ko as flags use karke space bachaya gaya. Interview favorite hai yeh one-liner looking but concept-heavy problem! 🔥
