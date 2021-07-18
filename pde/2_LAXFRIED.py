from util.Functions import *

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(levelname)s %(message)s')
logger = logging.getLogger(__name__)


appname="2_LAXFRIEDRICHS"
    

if __name__ == '__main__':
        
    logger.info("Starting {} =======================".format(appname))

    fn = Functions()
    u =fn.laxfried()
    norm, err = fn.initialize_arrays(2)
    
    fn.pre_plot(1)
    fn.plot([[fn.x_val,u],"u(x,T=0)"])
    
    
    for i,n in enumerate(pr.distance):
        un= fn.laxfried(u)
        norm = fn.add_to_array("norm",un,norm)
        if i in pr.selected_entries.keys():
            if i in pr.error_entries: err= fn.add_to_array("err",un,err)
            fn.plot([[fn.x_val,un],"u(x,T={})".format(str(pr.selected_entries[i]))])
        u= un
    logger.info("Performed {} iterations for Lax-Friedrichs and norm.".format(str(i)))
    
    fn.post_plot(appname,"x","u","Lax-Friedrichs Method","out")
    
    fn.pre_plot(2)
    fn.plot([[pr.distance,norm],""])
    fn.post_plot(appname,"t","L2 Norm","L2 Norm with Lax-Friedrichs Method","norm")
    
    fn.pre_plot(3)
    fn.plot([[pr.error_entries.values(),err,'o-'],""])
    fn.post_plot(appname,"t","Error of L2 Norm","Norma l2 per errore della soluzione con metodo Lax-Friedrichs","normerror")
    
    logger.info("======================= {} END".format(appname))