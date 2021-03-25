SELECT T2.[seriesname], 
       T0.[docnum], 
       T0.[folionum], 
       T0.[cardcode], 
       T0.[cardname], 
       T0.[docdate], 
       T1.[itemcode], 
       T1.[dscription], 
       T1.[quantity], 
       T1.[pricebefdi], 
       T1.[quantity] * T1.[price] AS TOTAL 
FROM   oinv T0 
       INNER JOIN inv1 T1 
               ON T0.[docentry] = T1.[docentry] 
       INNER JOIN nnm1 T2 
               ON T0.series = T2.series 
WHERE  T0.[docdate] >= [%0] 
       AND T0.[docdate] <= [%1] 
       AND T1.[itemcode] = '99999999999999999999' 
       AND T0.u_doc_declarable = 'S' 
UNION 
SELECT T2.[seriesname], 
       T0.[docnum], 
       T0.[folionum], 
       T0.[cardcode], 
       T0.[cardname], 
       T0.[docdate], 
       T1.[itemcode], 
       T1.[dscription], 
       T1.[quantity] * -1, 
       T1.[pricebefdi], 
       T1.[quantity] * T1.[price] * -1  AS TOTAL 
FROM   orin T0 
       INNER JOIN rin1 T1 
               ON T0.[docentry] = T1.[docentry] 
       INNER JOIN nnm1 T2 
               ON T0.series = T2.series 
WHERE  T0.[docdate] >= [%0] 
       AND T0.[docdate] <= [%1] 
       AND T1.[itemcode] = '99999999999999999999' 
       AND T0.u_doc_declarable = 'S' 


SELECT T2.[seriesname], 
       T0.[docnum], 
       T0.[folionum], 
       T0.[cardcode], 
       T0.[cardname], 
       T0.[docdate], 
       T1.[itemcode], 
       T1.[dscription], 
       T1.[quantity], 
       T1.[pricebefdi], 
       T1.[quantity] * T1.[price] AS TOTAL 
FROM   oinv T0 
       INNER JOIN inv1 T1 
               ON T0.[docentry] = T1.[docentry] 
       INNER JOIN nnm1 T2 
               ON T0.series = T2.series 
WHERE  T0.[docdate] >= [%0] 
       AND T0.[docdate] <= [%1] 
       AND T1.[itemcode] = '99999999999999999999' 
       AND T0.u_doc_declarable = 'S' 
UNION 
SELECT T2.[seriesname], 
       T0.[docnum], 
       T0.[folionum], 
       T0.[cardcode], 
       T0.[cardname], 
       T0.[docdate], 
       T1.[itemcode], 
       T1.[dscription], 
       T1.[quantity] * -1, 
       T1.[pricebefdi], 
       T1.[quantity] * T1.[price] * -1  AS TOTAL 
FROM   orin T0 
       INNER JOIN rin1 T1 
               ON T0.[docentry] = T1.[docentry] 
       INNER JOIN nnm1 T2 
               ON T0.series = T2.series 
WHERE  T0.[docdate] >= [%0] 
       AND T0.[docdate] <= [%1] 
       AND T1.[itemcode] = '99999999999999999999' 
       AND T0.u_doc_declarable = 'S' 

       