--
-- PostgreSQL database cluster dump
--

-- Started on 2024-12-13 20:19:24

SET default_transaction_read_only = off;

SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;

--
-- Roles
--

CREATE ROLE postgres;
ALTER ROLE postgres WITH SUPERUSER INHERIT CREATEROLE CREATEDB LOGIN REPLICATION BYPASSRLS;

--
-- User Configurations
--








--
-- Databases
--

--
-- Database "template1" dump
--

\connect template1

--
-- PostgreSQL database dump
--

-- Dumped from database version 17.2
-- Dumped by pg_dump version 17.2

-- Started on 2024-12-13 20:19:24

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET transaction_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

-- Completed on 2024-12-13 20:19:24

--
-- PostgreSQL database dump complete
--

--
-- Database "postgres" dump
--

\connect postgres

--
-- PostgreSQL database dump
--

-- Dumped from database version 17.2
-- Dumped by pg_dump version 17.2

-- Started on 2024-12-13 20:19:24

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET transaction_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- TOC entry 7 (class 2615 OID 16387)
-- Name: pgagent; Type: SCHEMA; Schema: -; Owner: postgres
--

CREATE SCHEMA pgagent;


ALTER SCHEMA pgagent OWNER TO postgres;

--
-- TOC entry 4955 (class 0 OID 0)
-- Dependencies: 7
-- Name: SCHEMA pgagent; Type: COMMENT; Schema: -; Owner: postgres
--

COMMENT ON SCHEMA pgagent IS 'pgAgent system tables';


--
-- TOC entry 2 (class 3079 OID 16388)
-- Name: pgagent; Type: EXTENSION; Schema: -; Owner: -
--

CREATE EXTENSION IF NOT EXISTS pgagent WITH SCHEMA pgagent;


--
-- TOC entry 4956 (class 0 OID 0)
-- Dependencies: 2
-- Name: EXTENSION pgagent; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION pgagent IS 'A PostgreSQL job scheduler';


--
-- TOC entry 4733 (class 0 OID 16389)
-- Dependencies: 223
-- Data for Name: pga_jobagent; Type: TABLE DATA; Schema: pgagent; Owner: postgres
--

COPY pgagent.pga_jobagent (jagpid, jaglogintime, jagstation) FROM stdin;
6056	2024-12-11 20:30:05.075789-05	DESKTOP-55JHJG6
\.


--
-- TOC entry 4734 (class 0 OID 16398)
-- Dependencies: 225
-- Data for Name: pga_jobclass; Type: TABLE DATA; Schema: pgagent; Owner: postgres
--

COPY pgagent.pga_jobclass (jclid, jclname) FROM stdin;
\.


--
-- TOC entry 4735 (class 0 OID 16408)
-- Dependencies: 227
-- Data for Name: pga_job; Type: TABLE DATA; Schema: pgagent; Owner: postgres
--

COPY pgagent.pga_job (jobid, jobjclid, jobname, jobdesc, jobhostagent, jobenabled, jobcreated, jobchanged, jobagentid, jobnextrun, joblastrun) FROM stdin;
\.


--
-- TOC entry 4737 (class 0 OID 16456)
-- Dependencies: 231
-- Data for Name: pga_schedule; Type: TABLE DATA; Schema: pgagent; Owner: postgres
--

COPY pgagent.pga_schedule (jscid, jscjobid, jscname, jscdesc, jscenabled, jscstart, jscend, jscminutes, jschours, jscweekdays, jscmonthdays, jscmonths) FROM stdin;
\.


--
-- TOC entry 4738 (class 0 OID 16484)
-- Dependencies: 233
-- Data for Name: pga_exception; Type: TABLE DATA; Schema: pgagent; Owner: postgres
--

COPY pgagent.pga_exception (jexid, jexscid, jexdate, jextime) FROM stdin;
\.


--
-- TOC entry 4739 (class 0 OID 16498)
-- Dependencies: 235
-- Data for Name: pga_joblog; Type: TABLE DATA; Schema: pgagent; Owner: postgres
--

COPY pgagent.pga_joblog (jlgid, jlgjobid, jlgstatus, jlgstart, jlgduration) FROM stdin;
\.


--
-- TOC entry 4736 (class 0 OID 16432)
-- Dependencies: 229
-- Data for Name: pga_jobstep; Type: TABLE DATA; Schema: pgagent; Owner: postgres
--

COPY pgagent.pga_jobstep (jstid, jstjobid, jstname, jstdesc, jstenabled, jstkind, jstcode, jstconnstr, jstdbname, jstonerror, jscnextrun) FROM stdin;
\.


--
-- TOC entry 4740 (class 0 OID 16514)
-- Dependencies: 237
-- Data for Name: pga_jobsteplog; Type: TABLE DATA; Schema: pgagent; Owner: postgres
--

COPY pgagent.pga_jobsteplog (jslid, jsljlgid, jsljstid, jslstatus, jslresult, jslstart, jslduration, jsloutput) FROM stdin;
\.


-- Completed on 2024-12-13 20:19:25

--
-- PostgreSQL database dump complete
--

--
-- Database "t0" dump
--

--
-- PostgreSQL database dump
--

-- Dumped from database version 17.2
-- Dumped by pg_dump version 17.2

-- Started on 2024-12-13 20:19:25

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET transaction_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- TOC entry 4883 (class 1262 OID 16634)
-- Name: t0; Type: DATABASE; Schema: -; Owner: postgres
--

CREATE DATABASE t0 WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'Spanish_Colombia.1252';


ALTER DATABASE t0 OWNER TO postgres;

\connect t0

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET transaction_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 217 (class 1259 OID 16635)
-- Name: categoria; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.categoria (
    id_categoria integer NOT NULL,
    nombre text NOT NULL,
    id_tienda integer
);


ALTER TABLE public.categoria OWNER TO postgres;

--
-- TOC entry 218 (class 1259 OID 16640)
-- Name: cliente; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.cliente (
    cc integer NOT NULL,
    nombre text NOT NULL,
    apellido text NOT NULL
);


ALTER TABLE public.cliente OWNER TO postgres;

--
-- TOC entry 219 (class 1259 OID 16645)
-- Name: comentario; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.comentario (
    id integer NOT NULL,
    coment text,
    cc_cliente integer
);


ALTER TABLE public.comentario OWNER TO postgres;

--
-- TOC entry 220 (class 1259 OID 16650)
-- Name: producto; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.producto (
    id integer NOT NULL,
    nombre text NOT NULL,
    "caracter¡stica" text,
    "descripci¢n " text,
    precio integer,
    stock integer,
    id_categoria integer,
    id_comentario integer
);


ALTER TABLE public.producto OWNER TO postgres;

--
-- TOC entry 221 (class 1259 OID 16655)
-- Name: tienda; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.tienda (
    id integer NOT NULL,
    nombre text NOT NULL,
    redes text,
    celular integer,
    direccion text
);


ALTER TABLE public.tienda OWNER TO postgres;

--
-- TOC entry 4873 (class 0 OID 16635)
-- Dependencies: 217
-- Data for Name: categoria; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.categoria (id_categoria, nombre, id_tienda) FROM stdin;
1	Electronica	1
2	Ropa	2
3	Accesorios	2
\.


--
-- TOC entry 4874 (class 0 OID 16640)
-- Dependencies: 218
-- Data for Name: cliente; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.cliente (cc, nombre, apellido) FROM stdin;
101	Carlos	P‚rez
102	Ana	Garc¡a
103	Luis	Mart¡nez
\.


--
-- TOC entry 4875 (class 0 OID 16645)
-- Dependencies: 219
-- Data for Name: comentario; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.comentario (id, coment, cc_cliente) FROM stdin;
\.


--
-- TOC entry 4876 (class 0 OID 16650)
-- Dependencies: 220
-- Data for Name: producto; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.producto (id, nombre, "caracter¡stica", "descripci¢n ", precio, stock, id_categoria, id_comentario) FROM stdin;
1	Laptop	16GB RAM	Laptop de alta gama	120000	10	1	\N
2	Camiseta	100% Algod¢n	Camiseta blanca b sica	20	50	2	\N
3	Aud¡fonos	Bluetooth	Aud¡fonos inal mbricos	50	30	3	\N
4	Pantalones	Jeans	Pantalones de mezclilla	40	25	2	\N
\.


--
-- TOC entry 4877 (class 0 OID 16655)
-- Dependencies: 221
-- Data for Name: tienda; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.tienda (id, nombre, redes, celular, direccion) FROM stdin;
2	Fashion Hub	@fashionhub	9876543	Avenida 456, Ciudad B
1	Tech Store	@techstore	123456	Calle 123, Ciudad A'
\.


--
-- TOC entry 4711 (class 2606 OID 16661)
-- Name: categoria categoria_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.categoria
    ADD CONSTRAINT categoria_pkey PRIMARY KEY (id_categoria);


--
-- TOC entry 4714 (class 2606 OID 16663)
-- Name: cliente cliente_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.cliente
    ADD CONSTRAINT cliente_pkey PRIMARY KEY (cc);


--
-- TOC entry 4716 (class 2606 OID 16665)
-- Name: comentario comentario_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.comentario
    ADD CONSTRAINT comentario_pkey PRIMARY KEY (id);


--
-- TOC entry 4721 (class 2606 OID 16686)
-- Name: producto producto_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.producto
    ADD CONSTRAINT producto_pkey PRIMARY KEY (id);


--
-- TOC entry 4723 (class 2606 OID 16688)
-- Name: tienda tienda_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.tienda
    ADD CONSTRAINT tienda_pkey PRIMARY KEY (id);


--
-- TOC entry 4717 (class 1259 OID 16666)
-- Name: fki_cc_cliente; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX fki_cc_cliente ON public.comentario USING btree (cc_cliente);


--
-- TOC entry 4718 (class 1259 OID 16667)
-- Name: fki_id_categoria; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX fki_id_categoria ON public.producto USING btree (id_categoria);


--
-- TOC entry 4719 (class 1259 OID 16668)
-- Name: fki_id_comentario; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX fki_id_comentario ON public.producto USING btree (id_comentario);


--
-- TOC entry 4712 (class 1259 OID 16669)
-- Name: fki_id_tienda; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX fki_id_tienda ON public.categoria USING btree (id_tienda);


--
-- TOC entry 4725 (class 2606 OID 16670)
-- Name: comentario cc_cliente; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.comentario
    ADD CONSTRAINT cc_cliente FOREIGN KEY (cc_cliente) REFERENCES public.cliente(cc) NOT VALID;


--
-- TOC entry 4726 (class 2606 OID 16675)
-- Name: producto id_categoria; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.producto
    ADD CONSTRAINT id_categoria FOREIGN KEY (id_categoria) REFERENCES public.categoria(id_categoria) NOT VALID;


--
-- TOC entry 4727 (class 2606 OID 16680)
-- Name: producto id_comentario; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.producto
    ADD CONSTRAINT id_comentario FOREIGN KEY (id_comentario) REFERENCES public.comentario(id) NOT VALID;


--
-- TOC entry 4724 (class 2606 OID 16689)
-- Name: categoria id_tienda; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.categoria
    ADD CONSTRAINT id_tienda FOREIGN KEY (id_tienda) REFERENCES public.tienda(id) NOT VALID;


-- Completed on 2024-12-13 20:19:25

--
-- PostgreSQL database dump complete
--

-- Completed on 2024-12-13 20:19:25

--
-- PostgreSQL database cluster dump complete
--

