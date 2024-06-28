from database.DB_connect import DBConnect
from model.gene import Gene


class DAO:
    def __init__(self):
        pass

    @staticmethod
    def getGene():
        cnx=DBConnect.get_connection()
        cursor=cnx.cursor(dictionary=True)
        query="""select distinctrow g.GeneID ,g.Essential ,g.Chromosome 
                        from genes_small.genes g 
                        where g.Essential ="Essential"  """
        cursor.execute(query)
        res=[]
        for a in cursor:
            res.append(Gene(**a))
        cursor.close()
        cnx.close()
        return res

    @staticmethod
    def getArchiUguali():
        cnx=DBConnect.get_connection()
        cursor=cnx.cursor(dictionary=False)
        query="""select distinctrow i.GeneID1 ,i.GeneID2 , abs(  i.Expression_Corr )*2 valore
                from genes_small.interactions i ,
                (select distinct g.GeneID, g.Chromosome
                from genes_small.genes g
                where g.Essential ="Essential") g,
                (select distinct g.GeneID, g.Chromosome
                from genes_small.genes g
                where g.Essential ="Essential") g2
                where i.GeneID1 <> i.GeneID2 
                and i.GeneID1 =g.GeneID
                and i.GeneID2 = g2.GeneID 
                and g.Chromosome = g2.Chromosome
                order by i.GeneID1"""
        cursor.execute(query)
        res=[]
        for a in cursor:
            res.append(a)
        cursor.close()
        cnx.close()
        return res

    @staticmethod
    def getArchiDiversi():
        cnx=DBConnect.get_connection()
        cursor=cnx.cursor(dictionary=False)
        query="""select distinctrow i.GeneID1 ,i.GeneID2 , abs(  i.Expression_Corr ) valore
                from genes_small.interactions i ,
                (select distinct g.GeneID, g.Chromosome
                from genes_small.genes g
                where g.Essential ="Essential") g,
                (select distinct g.GeneID, g.Chromosome
                from genes_small.genes g
                where g.Essential ="Essential") g2
                where i.GeneID1 <> i.GeneID2 
                and i.GeneID1 =g.GeneID
                and i.GeneID2 = g2.GeneID 
                and g.Chromosome <> g2.Chromosome
                order by i.GeneID1 """
        cursor.execute(query)
        res=[]
        for a in cursor:
            res.append(a)
        cursor.close()
        cnx.close()
        return res