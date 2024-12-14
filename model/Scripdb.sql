
CREATE TABLE public."categoria" (
    "id_categoria" integer NOT NULL,
    "nombre" text NOT NULL,
    "id_tienda" integer
);


ALTER TABLE public."categoria" OWNER TO postgres;

CREATE TABLE public."cliente" (
    "cc" integer NOT NULL,
    "nombre" text NOT NULL,
    "apellido" text NOT NULL
);


ALTER TABLE public."cliente" OWNER TO postgres;

CREATE TABLE public."comentario" (
    "id" integer NOT NULL,
    "coment" text,
    "cc_cliente" integer
);


ALTER TABLE public."comentario" OWNER TO postgres;

CREATE TABLE public."producto" (
    "id" integer NOT NULL,
    "nombre" text NOT NULL,
    "id_categoria" integer,
    
);


ALTER TABLE public."producto" OWNER TO postgres;

CREATE TABLE public."tienda" (
    "id" integer NOT NULL,
    "nombre" text NOT NULL,
    "redes" text,
    "celular" integer,
    "direccion" text
);


ALTER TABLE public."tienda" OWNER TO postgres;

CREATE TABLE public."campos_de_formularios" (
    "id" integer ,
    "nombre" text,
    "tipo" text ,
    "formato" text,
    "libreria" text,
    "nombre_letrero" text,
    "isEnable" integer
);


ALTER TABLE public."campos_de_formularios" OWNER TO postgres;

CREATE TABLE public."librerias" (
    "id" integer ,
    "key" integer ,
    "valor" text ,
    "tp_libreria" text
  );
 
ALTER TABLE public."librerias" OWNER TO postgres;

CREATE TABLE public."tienda_producto" (
    "id" integer, 
    "precio" integer,
    "calificacion" integer,
    "stock" integer,
    "caracteristicas" text,
    "descripcion" text,
    "id_tienda" integer NOT NULL,
    "id_producto" integer NOT NULL,
    "id_comentario" integer,
    PRIMARY KEY ("id_tienda", "id_producto")
);

ALTER TABLE public."tienda_producto" OWNER TO postgres;



COPY public."cliente" ("cc", "nombre", "apellido") FROM stdin;
201	Juana	Pérez
202	Carlos	Mendoza
203	Luisa	Gómez
\.
COPY public."comentario" (id, "coment", "cc_cliente") FROM stdin;
1   "El queso es muy fresco y delicioso."   201
2   "Los plátanos están en excelente estado."   202
3   "Los huevos son de excelente calidad."   203
\.

COPY public."tienda" ("id", "nombre", "redes", "celular", "direccion") FROM stdin;
1	Delicias de la Sierra	@delicias_sierra	5551234	Aldea Alta
2	Granja Los Fresnos	@granjalosfresnos	5554321	Finca 23
3	Granja Los Fresnos	@granjalosfresnos	5554321	Finca 23
\.


COPY public."categoria" ("id_categoria", "nombre", "id_tienda") FROM stdin;
1	Lácteos	3
2	Frutas	3
3	Huevos	3
\.


COPY public."producto" ("id", "nombre", "caracteristica", "descripcion ", "precio", "stock", "id_categoria", "id_comentario") FROM stdin;
1	Queso	Fresco	Queso artesanal producido localmente	15	50	1	1
2	Plátano	Orgánico	Plátanos cosechados sin químicos	5	100	2	2
3	Huevos	Gallinas libres	Huevos frescos de granja	10	80	3	3
\.



COPY public."tienda_producto" ("id", "precio", "stock", "caracteristica", "id_tienda", "id_producto", "id_comentario", "calificacion", "descripcion")
FROM stdin;
1   1500    100   "Orgánico, artesanal"          1   1   10    5   "Queso fresco de alta calidad"
2   500     200   "Cultivado sin pesticidas"     1   2   11    4   "Plátanos orgánicos cultivados localmente"
3   1000    80    "Rico en omega-3"              1   3   12    5   "Huevos frescos de gallinas libres"
\.

COPY public."campos_de_formularios" ("id", "nombre", "tipo", "formato", "libreria", "nombre_letrero", "isEnable") FROM stdin;
1   "Cantidad"  "Número"  "Numérico"    "UI/UX"   "Ingrese la cantidad"   1
2   "Producto"  "Texto"   "Alfanumérico" "UI/UX"   "Ingrese el nombre del producto"   1
\.

COPY public."librerias" ("id", "key", "valor", "tp_libreria") FROM stdin;
1   201   "Queso fresco artesanal"   "Agro"
2   202   "Plátanos orgánicos"       "Agro"
3   203   "Huevos de gallinas libres" "Agro"
\.





ALTER TABLE ONLY public."categoria"
    ADD CONSTRAINT "categoria_pkey" PRIMARY KEY ("id_categoria");

ALTER TABLE ONLY public."librerias"
    ADD CONSTRAINT "librerias_pkey" PRIMARY KEY ("id");

    ALTER TABLE ONLY public."tienda_producto"
    ADD CONSTRAINT "fk_tienda" FOREIGN KEY ("id_tienda") REFERENCES public."tienda"("id");

ALTER TABLE ONLY public."tienda_producto"
    ADD CONSTRAINT "fk_producto" FOREIGN KEY ("id_producto") REFERENCES public."producto"("id");


ALTER TABLE ONLY public."campos_de_formularios"
    ADD CONSTRAINT "campos_de_formularios_pkey" PRIMARY KEY ("id");


ALTER TABLE ONLY public."cliente"
    ADD CONSTRAINT "cliente_pkey" PRIMARY KEY ("cc");

ALTER TABLE ONLY public."comentario"
    ADD CONSTRAINT "comentario_pkey" PRIMARY KEY ("id");

ALTER TABLE ONLY public."producto"
    ADD CONSTRAINT "producto_pkey" PRIMARY KEY ("id");

ALTER TABLE ONLY public."tienda"
    ADD CONSTRAINT "tienda_pkey" PRIMARY KEY ("id");


CREATE INDEX "fki_cc_cliente" ON public."comentario" USING btree ("cc_cliente");

CREATE INDEX "fki_id_categoria" ON public."producto" USING btree ("id_categoria");

CREATE INDEX "fki_id_comentario" ON public."producto" USING btree ("id_comentario");

CREATE INDEX "fki_id_tienda" ON public."categoria" USING btree ("id_tienda");

CREATE INDEX "idx_tienda_producto_tienda" ON public."tienda_producto" USING btree ("id_tienda");

CREATE INDEX "idx_tienda_producto_producto" ON public."tienda_producto" USING btree ("id_producto");

ALTER TABLE ONLY public."comentario"
    ADD CONSTRAINT "cc_cliente" FOREIGN KEY ("cc_cliente") REFERENCES public."cliente"("cc") NOT VALID;

ALTER TABLE ONLY public."producto"
    ADD CONSTRAINT "id_categoria" FOREIGN KEY ("id_categoria") REFERENCES public."categoria"("id_categoria") NOT VALID;

ALTER TABLE ONLY public."producto"
    ADD CONSTRAINT "id_comentario" FOREIGN KEY ("id_comentario") REFERENCES public."comentario"(id) NOT VALID;

ALTER TABLE ONLY public."categoria"
    ADD CONSTRAINT "id_tienda" FOREIGN KEY ("id_tienda") REFERENCES public."tienda"("id") NOT VALID;

ALTER TABLE ONLY public."comentario"
    VALIDATE CONSTRAINT "cc_cliente";

ALTER TABLE ONLY public."producto"
    VALIDATE CONSTRAINT "id_categoria";

ALTER TABLE ONLY public."producto"
    VALIDATE CONSTRAINT "id_comentario";

ALTER TABLE ONLY public."categoria"
    VALIDATE CONSTRAINT "id_tienda";
