1. The training part is the model building process:
(1) When running the training.py code, pay attention to modify the address at the beginning of the program to read the data and the model storage address as needed. Three parallel CNN training needs to run the code three times. Each time select the corresponding data address and model address;
(3) The three folders modelxy, modelxz, and modelyz in the model folder are the models saved after training, which can be directly called to predict new proteins.

2. The preprocessing part 
It is the process of using PDB files to generate the pictures needed for the training model:
The feature_extraction.py program processes all PDB files in a folder at a time, so the address of the read data needs to be modified according to the situation. There are two addresses that need to be modified. Run the code twice, it is best to add the address of the picture to be saved in the last picture saving statement, otherwise all pictures are generated in the current folder by default
     
3. Prediction part can call the model to predict the new protein:
(1) First use preprocessing to convert the PDB file into pictures corresponding to the three projection directions;
(2) Predictionxy, predictionxz, predictionyz three .py files respectively call a CNN training result to make predictions on the projected picture in one direction,
?????The model address in the existing code is the absolute path saved by the model on the server and can be used directly. If you need to retrain, you can change the path by modifying the path.
?????The current model is replaced with the newly trained model, and the results of the operation are written into a .txt file;
(3) The three .txt files of xy, xz, and yz are the running result files of the example protein, which will be overwritten when predicting new proteins;
(4) The integrate.py program votes on the results of the above three .txt files. The current default voting mechanism is the majority voting system, and the accuracy rate of disease protein prediction is 0.92.
?????However, the false negative rate may be relatively high. The output result is the protein PDB ID and the number of votes obtained. The higher the number of votes, the greater the possibility of illness;     


   