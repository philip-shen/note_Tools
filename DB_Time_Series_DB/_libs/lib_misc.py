from _libs.logger_setup import *
import os,glob

__all__ = [
#
    'format_time',
    'Query_all_files_in_dir',
    'Diff_List',

]

def format_time(timesec):
    m, s = divmod(timesec, 60)
    h, m = divmod(m, 60)
    str_format_time= ''
    if h == 0:
        if m == 0:
            str_format_time= "%02ds" % (s)
            #return "%02ds" % (s)
        else:
            str_format_time= "%02dm%02ds" % (m, s)
            #return "%02dm%02ds" % (m, s)
    else:
        str_format_time= "%dh%02dm%02ds" % (h, m, s)
        #return "%dh%02dm%02ds" % (h, m, s)

    return str_format_time, h, m, s


def walk_in_dir(dir_path,file_type,opt_verbose='OFF'):
    ret_listOfFileNames = []
    
    for filename in glob.glob(os.path.join(dir_path, file_type)):
        listOfFileNames = []

        listOfFileNames = filename
        ret_listOfFileNames.append(listOfFileNames)

        
        if opt_verbose.lower() == "on":
            msg = "fileName:{} in directory:{}"
            logger.info(msg.format(filename, dir_path))
             
            msg = "listOfFileNames:{} in walk_in_dir"
            logger.info(msg.format(listOfFileNames))        

    for dirname in (d for d in os.listdir(dir_path) if os.path.isdir(os.path.join(dir_path, d)) ):
        walk_in_dir(os.path.join(dir_path, dirname),file_type)
        
    if opt_verbose.lower() == "on":
        msg = "number of listOfFileNames:{} in walk_in_dir"
        logger.info(msg.format( len(ret_listOfFileNames) ))
        msg = "ret_listOfFileNames:{} in walk_in_dir"
        logger.info(msg.format(ret_listOfFileNames))        

    return ret_listOfFileNames
class Query_all_files_in_dir:

    def __init__(self,dir_path,file_type,opt_verbose='OFF'):
        self.dir_path= dir_path
        self.file_type= file_type
        self.opt_verbose= opt_verbose
        self.ret_listOfFileNames= []

    def walk_in_dir(self):

        for filename in glob.glob(os.path.join(self.dir_path, self.file_type)):
            listOfFileNames = []

            listOfFileNames = filename
            self.ret_listOfFileNames.append(listOfFileNames)

            if self.opt_verbose.lower() == "on":
                msg = "fileName:{} in directory:{}"
                logger.info(msg.format(filename, self.dir_path))
             
                msg = "listOfFileNames:{} in walk_in_dir"
                logger.info(msg.format(listOfFileNames))      

        for dirname in (d for d in os.listdir(self.dir_path) if os.path.isdir(os.path.join(self.dir_path, d)) ):
            walk_in_dir(os.path.join(self.dir_path, dirname), self.file_type, self.opt_verbose)

        '''
        number of self.ret_listOfFileNames:8 in walk_in_dir
        '''        
        '''
        self.ret_listOfFileNames:['/home/philip.shen/Wov_Test/auto_tools/dbg_2020-10-13_144554.log', 
        '/home/philip.shen/Wov_Test/auto_tools/dbg_2020-10-13_164632.log', 
        '/home/philip.shen/Wov_Test/auto_tools/dbg_2020-10-13_184703.log', 
        '/home/philip.shen/Wov_Test/auto_tools/dbg_2020-10-13_193507.log', 
        '/home/philip.shen/Wov_Test/auto_tools/dbg_2020-10-13_200110.log', 
        '/home/philip.shen/Wov_Test/auto_tools/dbg_2020-10-13_220142.log', 
        '/home/philip.shen/Wov_Test/auto_tools/dbg_2020-10-14_000214.log', 
        '/home/philip.shen/Wov_Test/auto_tools/dbg_2020-10-14_020246.log'] in walk_in_dir
        '''
        if self.opt_verbose.lower() == "on":
            msg = "number of self.ret_listOfFileNames:{} in walk_in_dir"
            logger.info(msg.format( len(self.ret_listOfFileNames) ))
            msg = "self.ret_listOfFileNames:{} in walk_in_dir"
            logger.info(msg.format(self.ret_listOfFileNames))        

        return self.ret_listOfFileNames    
    
def Diff_List(li1, li2):
    li_dif = [i for i in li1 + li2 if i not in li1 or i not in li2]
    return li_dif