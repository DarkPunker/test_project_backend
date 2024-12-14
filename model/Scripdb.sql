
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
    "característica" text,
    "descripción " text,
    "precio" integer,
    "stock" integer,
    "id_categoria" integer,
    "id_comentario" integer
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

COPY public."categoria" ("id_categoria", "nombre", "id_tienda") FROM stdin;
1	Electronica	1
2	Ropa	2
3	Accesorios	2
\.


COPY public."cliente" ("cc", "nombre", "apellido") FROM stdin;
101	Carlos	Pérez
102	Ana	García
103	Luis	Martínez
\.


COPY public."comentario" (id, "coment", "cc_cliente") FROM stdin;
\.


COPY public."producto" ("id", "nombre", "característica", "descripción ", "precio", "stock", "id_categoria", "id_comentario") FROM stdin;
1	Laptop	16GB RAM	Laptop de alta gama	120000	10	1	\N
2	Camiseta	100% Algodón	Camiseta blanca básica	20	50	2	\N
3	Audífonos	Bluetooth	Audífonos inalámbricos	50	30	3	\N
4	Pantalones	Jeans	Pantalones de mezclilla	40	25	2	\N
\.


COPY public."tienda" ("id", "nombre", "redes", "celular", "direccion") FROM stdin;
2	Fashion Hub	@fashionhub	9876543	Avenida 456, Ciudad B
1	Tech Store	@techstore	123456	Calle 123, Ciudad A'
\.


ALTER TABLE ONLY public."categoria"
    ADD CONSTRAINT "categoria_pkey" PRIMARY KEY ("id_categoria");

ALTER TABLE ONLY public."librerias"
    ADD CONSTRAINT "librerias_pkey" PRIMARY KEY ("id");


ALTER TABLE ONLY public."campos_de_formularios"
    ADD CONSTRAINT "campos_de_formularios_pkey" PRIMARY KEY ("id");


ALTER TABLE ONLY public."cliente"
    ADD CONSTRAINT "cliente_pkey" PRIMARY KEY ("cc");

ALTER TABLE ONLY public."comentario"
    ADD CONSTRAINT "comentario_pkey" PRIMARY KEY (id);

ALTER TABLE ONLY public."producto"
    ADD CONSTRAINT "producto_pkey" PRIMARY KEY ("id");

ALTER TABLE ONLY public."tienda"
    ADD CONSTRAINT "tienda_pkey" PRIMARY KEY ("id");


CREATE INDEX "fki_cc_cliente" ON public."comentario" USING btree ("cc_cliente");

CREATE INDEX "fki_id_categoria" ON public."producto" USING btree ("id_categoria");

CREATE INDEX "fki_id_comentario" ON public."producto" USING btree ("id_comentario");

CREATE INDEX "fki_id_tienda" ON public."categoria" USING btree ("id_tienda");

ALTER TABLE ONLY public."comentario"
    ADD CONSTRAINT "cc_cliente" FOREIGN KEY ("cc_cliente") REFERENCES public."cliente"("cc") NOT VALID;

ALTER TABLE ONLY public."producto"
    ADD CONSTRAINT "id_categoria" FOREIGN KEY ("id_categoria") REFERENCES public."categoria"("id_categoria") NOT VALID;

ALTER TABLE ONLY public."producto"
    ADD CONSTRAINT "id_comentario" FOREIGN KEY ("id_comentario") REFERENCES public."comentario"(id) NOT VALID;

ALTER TABLE ONLY public."categoria"
    ADD CONSTRAINT "id_tienda" FOREIGN KEY ("id_tienda") REFERENCES public."tienda"("id") NOT VALID;
