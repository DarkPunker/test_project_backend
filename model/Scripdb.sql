CREATE SEQUENCE "inc_id_categoria";

CREATE TABLE public."categoria" (
    "id" integer PRIMARY KEY DEFAULT nextval('inc_id_categoria'),
    "nombre" text NOT NULL,
    "id_tienda" integer
);


ALTER TABLE public."categoria" OWNER TO postgres;

CREATE TABLE public."cliente" (
    "cc" integer NOT NULL,
    "nombre" text NOT NULL,
    "apellido" text NOT NULL,
    "direccion" text,
    "lat" text,
    "long" text,
    "id_usuario" integer NOT NULL
);


ALTER TABLE public."cliente" OWNER TO postgres;

CREATE SEQUENCE "inc_id_orden_compra";

CREATE TABLE public."orden_compra" (
    "id" integer PRIMARY KEY DEFAULT nextval('inc_id_orden_compra'),
    "comentario" text,
    "cantidad" numeric,
    "calificacion" numeric,
    "estado" integer,
    "cc_cliente" integer,
    "id_tienda_producto" integer
);


ALTER TABLE public."orden_compra" OWNER TO postgres;

CREATE SEQUENCE "inc_id_producto";
CREATE TABLE public."producto" (
    "id" integer PRIMARY KEY DEFAULT nextval('inc_id_producto'),
    "nombre" text NOT NULL,
    "unidad_medida" text,
    "id_categoria" integer
);


ALTER TABLE public."producto" OWNER TO postgres;

CREATE SEQUENCE "inc_id_tienda";
CREATE TABLE public."tienda" (
    "id" integer PRIMARY KEY DEFAULT nextval('inc_id_tienda'),
    "nombre" text NOT NULL,
    "redes" text,
    "celular" integer,
    "direccion" text,
    "lat" text,
    "long" text,
    "id_usuario" integer NOT NULL
);


ALTER TABLE public."tienda" OWNER TO postgres;

CREATE TABLE public."campos_de_formularios" (
    "id" integer,
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

CREATE SEQUENCE "inc_id_tienda_producto";

CREATE TABLE public."tienda_producto" (
    "id" integer PRIMARY KEY DEFAULT nextval('inc_id_tienda_producto'),
    "precio" integer,
    "calificacion" numeric,
    "stock" numeric,
    "caracteristicas" text,
    "descripcion" text,
    "id_tienda" integer NOT NULL,
    "id_producto" integer NOT NULL
);

ALTER TABLE public."tienda_producto" OWNER TO postgres;

CREATE SEQUENCE "inc_id_usuario";

CREATE TABLE public."usuario" (
    "id" integer PRIMARY KEY DEFAULT nextval('inc_id_usuario'),
    "email" text NOT NULL,
    "contrasena" text NOT NULL
);

ALTER TABLE public."usuario" OWNER TO postgres;

ALTER TABLE ONLY public."usuario"
    ADD CONSTRAINT "usuario_pkey" PRIMARY KEY ("id");

ALTER TABLE ONLY public."campos_de_formularios"
    ADD CONSTRAINT "campos_de_formularios_pkey" PRIMARY KEY ("id");

ALTER TABLE ONLY public."librerias"
    ADD CONSTRAINT "librerias_pkey" PRIMARY KEY ("id");


ALTER TABLE ONLY public."cliente"
    ADD CONSTRAINT "cliente_pkey" PRIMARY KEY ("cc");

ALTER TABLE ONLY public."tienda_producto"
    ADD CONSTRAINT "fk_tienda" FOREIGN KEY ("id_tienda") REFERENCES public."tienda"("id");

ALTER TABLE ONLY public."tienda_producto"
    ADD CONSTRAINT "fk_producto" FOREIGN KEY ("id_producto") REFERENCES public."producto"("id");

ALTER TABLE ONLY public."orden_compra"
    ADD CONSTRAINT "fk_cliente" FOREIGN KEY ("cc_cliente") REFERENCES public."cliente"("cc") NOT VALID;
ALTER TABLE ONLY public."orden_compra"
    ADD CONSTRAINT "fk_tienda_producto" FOREIGN KEY ("id_tienda_producto") REFERENCES public."tienda_producto"("id") NOT VALID;

ALTER TABLE ONLY public."producto"
    ADD CONSTRAINT "fk_categoria" FOREIGN KEY ("id_categoria") REFERENCES public."categoria"("id") NOT VALID;

ALTER TABLE ONLY public."categoria"
    ADD CONSTRAINT "fk_tienda" FOREIGN KEY ("id_tienda") REFERENCES public."tienda"("id") NOT VALID;

ALTER TABLE ONLY public."cliente"
    ADD CONSTRAINT "fk_usuario" FOREIGN KEY ("id_usuario") REFERENCES public."usuario"("id") NOT VALID;


CREATE INDEX "fki_cc_cliente" ON public."orden_compra" USING btree ("cc_cliente");

CREATE INDEX "fki_id_categoria" ON public."producto" USING btree ("id_categoria");

CREATE INDEX "fki_id_tienda" ON public."categoria" USING btree ("id_tienda");

CREATE INDEX "idx_tienda_producto_tienda" ON public."tienda_producto" USING btree ("id_tienda");

CREATE INDEX "idx_tienda_producto_producto" ON public."tienda_producto" USING btree ("id_producto");

-- TRUNCATE TABLE
--  cliente,
--  comentario,
--  categoria,
--  producto,
--  tienda,
--  campos_de_formularios,
--  librerias,
--  tienda_producto,
--  usuario
-- CASCADE;
