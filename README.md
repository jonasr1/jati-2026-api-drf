# 🍽 Restaurant Reservation API – Django + DRF Challenge

## 📌 Overview

Neste desafio, você irá desenvolver uma API RESTful para gerenciamento de reservas de mesas em um restaurante utilizando **Django** e **Django REST Framework (DRF)**.

O objetivo é aplicar conceitos fundamentais de backend:

* Modelagem relacional
* Autenticação com JWT
* Regras de negócio
* Validação de dados
* Permissões de acesso
* Consultas eficientes com ORM

Este projeto simula um sistema real de reservas, incluindo controle de disponibilidade e restrições de acesso.

---

## 🛠 Tech Stack

* Python 3.12+
* Django
* Django REST Framework
* SimpleJWT
* PostgreSQL ou SQLite
* django-filter (opcional)

---

## 🎯 Objetivo Principal

Construir uma API capaz de:

* Gerenciar usuários com autenticação JWT
* Gerenciar mesas do restaurante
* Criar e cancelar reservas
* Validar disponibilidade e capacidade
* Controlar permissões de acesso

---

## 📦 Entidades do Sistema

## 👤 User

O projeto utilizará o modelo padrão de usuário do Django (django.contrib.auth).

Campos principais:

* id
* username
* email
* password (armazenada com hash)
* is_staff
* is_superuser

Regras:

* Usuários autenticados podem criar e visualizar suas próprias reservas.
* Apenas usuários com is_staff = True podem gerenciar mesas.
* Usuários com is_staff = False são considerados clientes.

---

## 🪑 Table (Mesa)

Campos:

* id
* name
* capacity (número máximo de pessoas)
* is_active (boolean)

Regras:

* Apenas usuários com is_staff = True podem:
  * Criar mesas
  * Atualizar mesas
  * Remover mesas
  * Usuários comuns (is_staff = False) são considerados clientes.
* Mesas inativas não podem receber reservas.
* A disponibilidade da mesa deve ser calculada dinamicamente com base nas reservas ativas.

---

## 📅 Reservation

Campos:

* id
* user (FK para User)
* table (FK para Table)
* reservation_datetime
* number_of_people
* status (`active`, `canceled`)

Regras:

* A reserva deve ser feita apenas para datas futuras.
* A reserva deve estar dentro do horário de funcionamento do restaurante.
* O número de pessoas não pode ultrapassar a capacidade da mesa.
* Não pode existir conflito de horário para a mesma mesa.
* Apenas o usuário que criou a reserva pode cancelá-la.

---

## ⏰ Horário de Funcionamento

O restaurante funciona diariamente das:

18:00 às 23:00

Reservas fora desse intervalo devem ser rejeitadas.

---

## 📌 Regras de Negócio

## 1️⃣ Validação de Data

* Não permitir reservas no passado.
* Validar formato correto de data e hora.

---

## 2️⃣ Validação de Capacidade

* `number_of_people` não pode ser maior que `table.capacity`.

---

## 3️⃣ Conflito de Horário

Antes de criar uma reserva, o sistema deve verificar:

* Se já existe uma reserva ativa para a mesma mesa
* No mesmo horário (ou dentro do intervalo considerado ocupado)

Sugestão: considere que cada reserva ocupa 1 hora.

---

## 4️⃣ Cancelamento

* Apenas reservas com status `active` podem ser canceladas.
* Ao cancelar, o status deve mudar para `canceled`.

---

## 🔐 Autenticação

Utilize JWT para autenticação.

Endpoints obrigatórios:

* Registro de usuário
* Login
* Refresh token

Apenas usuários autenticados podem:

* Criar reservas
* Visualizar suas reservas
* Cancelar reservas

---

## 📡 Endpoints Obrigatórios

## 🔑 Authentication

* POST /api/auth/register
* POST /api/auth/login
* POST /api/auth/refresh

---

## 🪑 Tables

* GET /api/tables
* POST /api/tables (admin only)
* PATCH /api/tables/{id} (admin only)
* DELETE /api/tables/{id} (admin only)

---

## 📅 Reservations

* POST /api/reservations
* GET /api/reservations (apenas reservas do usuário autenticado)
* PATCH /api/reservations/{id}/cancel

---

## 🛡 Permissões

* Apenas administradores podem gerenciar mesas.
* Usuários só podem visualizar suas próprias reservas.
* Usuários só podem cancelar reservas que criaram.

---

## 📎 Validações Obrigatórias

* Campos obrigatórios devem ser validados.
* Datas devem estar no formato ISO 8601.
* Capacidade deve ser número positivo.
* Não permitir reserva se a mesa estiver inativa.

---

## 🧪 Critérios de Avaliação

* Organização do projeto
* Clareza na modelagem
* Implementação correta das regras de negócio
* Uso adequado do ORM
* Segurança e controle de permissões
* Código limpo e legível

---

## ⭐ Desafios Extras (Opcional)

### 1. Customização do User Model

Como desafio adicional, implemente um modelo de usuário customizado com as seguintes características:

* Login utilizando email como campo principal
* Remover o campo username
* Criar um campo role com opções:

  Ex:
  * Waiter
  * customer
  * admin

Dicas:

* Utilize AbstractUser
* Configure AUTH_USER_MODEL
* Implemente um CustomUserManager
* Atualize as ForeignKeys para usar settings.AUTH_USER_MODEL

### 2. Funcionalidades Intermediárias

* Implementar filtros por data e status
* Implementar paginação
* Criar endpoint para listar mesas disponíveis em determinada data
* Adicionar testes automatizados
