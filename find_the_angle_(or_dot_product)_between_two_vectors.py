# %%
"""
###   Calculate the angle between two vectors

* Given he Vectors 
$$
\vec{v}_{1} = \begin{bmatrix}5\\9\\\text{-1}\\0\end{bmatrix}, \vec{v}_{2} = \begin{bmatrix}7\\3\\9\\1\end{bmatrix}
$$

The dot product of these is given byn the following formula:

* Dot product:
$$
\vec{v}_1\vec{v}_{2} = ||\vec{v}_{1}||\cdot||\vec{v}_{2}|| \cdot cos\theta \\[0.5in]
$$

$$
\vec{v}_1\vec{v}_{2} = ||\begin{bmatrix}5\\9\\\text{-1}\\0\end{bmatrix}|| \cdot ||\begin{bmatrix}7\\3\\9\\1\end{bmatrix}|| \cdot cos\theta
$$

* The Angle (Theta) between these two vectors can be calculated in the following way:
$$
\theta = arcos(\frac{\vec{v}\cdot\vec{w}}{||\vec{v}||\cdot||\vec{w}||}) \\[0.5in]
$$

$$
\theta = arcos(\frac{\begin{bmatrix}5\\9\\\text{-1}\\0\end{bmatrix} \cdot \begin{bmatrix}7\\3\\9\\1\end{bmatrix}}{||\begin{bmatrix}5\\9\\\text{-1}\\0\end{bmatrix}|| \cdot ||\begin{bmatrix}7\\3\\9\\1\end{bmatrix}||}\\[0.5in]
$$

$$
\theta = arcos(\frac{5 \cdot 7 + 9 \cdot 3 + (-1) \cdot 9 + 0 \cdot 1}{\sqrt{5^2 + 9^2 + (-1)^2 + 0^2} \cdot \sqrt{7^2 + 3^2 + 9^2 + 1^2}})\\[0.5in]
$$

$$
\theta = arcos(\frac{53}{\sqrt{107} \cdot \sqrt{140}})\\[0.5in]
$$

$$
\theta = arcos(\frac{53}{\sqrt{14980}})
$$
"""

# %%
import numpy as np

v1 = np.array([5, 9, -1, 0]).T
v2 = np.array([7, 3, 9, 1]).T

result = np.matmul(v1, v2)

norm_v1 = np.linalg.norm(v1)
norm_v2 = np.linalg.norm(v2)

angle = np.arccos(result / (norm_v1 * norm_v2))
print('Angle in Radians: '+ str(angle))
print('Angle in Degrees: '+ str(np.degrees(angle)))

# %%
"""
Result:

$52.0148327°$
"""