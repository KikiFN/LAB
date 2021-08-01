from util.Functions import *
from FTCS import *
from LAXWENDROFF import err as lwerr
from LAXFRIED import err as lferr
from LEAPFROG import err as lperr

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(levelname)s %(message)s')
logger = logging.getLogger(__name__)


appname="5_ERRORS"
    

if __name__ == '__main__':
        
    logger.info("Starting {} =======================".format(appname))

    fn = Functions()

    fn.pre_plot(1)
    logger.info("Pre-plot ok, starting printing errors graph")
    fn.plot([[pr.error_entries.values(),lferr,'o-'],"Lax-Friedrichs"])
    fn.plot([[pr.error_entries.values(),lwerr,'o-'],"Lax-Wendroff"])
    fn.plot([[pr.error_entries.values(),lperr,'o-'],"Leapfrog"])
    fn.post_plot(appname,"t","Error of L2 Norm","Norma l2 per errore della soluzione con metodi LF,LW,LEAPFROG","normerror")
    logger.info("Done printing errors graph")
    
    logger.info("======================= {} END".format(appname))