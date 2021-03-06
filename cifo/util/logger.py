from copy import deepcopy
import pandas as pd
import os


class GeneticAlgorithmLogger:
    """
        Save a file for each run (search) of a genetic algorithm
    """
    #
    #----------------------------------------------------------------------------------------------
    def __init__(self, log_dir, log_name, run):
        self._log_name      = log_name
        self._log_dir       = log_dir
        self._run           = run
        self._runs          = []
        self._generations   = []
        self._fitness       = []

    #
    #----------------------------------------------------------------------------------------------    
    def add(self, generation, solution):
        self._runs.append(self._run)
        self._generations.append(generation)
        self._fitness.append(solution.fitness)  # adds the fittest solution of each generation

    #
    #----------------------------------------------------------------------------------------------  
    def save(self):
        
        final_log_dir   = str(self._log_dir) + str(self._log_name)
        file_name = f"/run_{self._run}.xlsx"  
        
        print(f'log: {final_log_dir + file_name}')

        df = pd.DataFrame(
            list(
                zip(
                    self._runs, 
                    self._generations, 
                    self._fitness
                )
            ), 
            columns =['Run', 'Generation', 'Fitness']
        )

        if not os.path.exists(final_log_dir):
            os.mkdir(final_log_dir)

        df.to_excel(final_log_dir + file_name, index = False, encoding = 'utf-8')
