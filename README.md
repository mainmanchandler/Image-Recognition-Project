Image Recognition Project in Python
--
Project by Samson Goodenough and I for our Image Processing and Recognition Class.

In our Python OpenCV image recognition project, we opted to utilize OpenCV's SIFT (Scale-Invariant Feature Transform) algorithm along with the Brute-Force matcher to facilitate the crucial tasks of feature extraction and matching between scene and object images. This approach was selected due to its perceived robustness, accessibility, and logical coherence in employing SIFT for object detection. To commence the process, we instantiated a SIFT object to generate keypoints and descriptors for each image using the detectAndCompute method. Subsequently, the Brute-Force object was employed to execute the matching of descriptors between the images, which was followed by a ratio test aimed at discerning and filtering out matching and non-matching features.
