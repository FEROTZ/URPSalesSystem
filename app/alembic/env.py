# import sys
# from pathlib import Path

# # Ajusta la ruta del proyecto
# project_root = Path(__file__).parents[2].resolve()
# sys.path.insert(0, str(project_root))

# from logging.config import fileConfig

# from sqlalchemy import engine_from_config
# from sqlalchemy import pool

# from alembic import context

# # Importa directamente los modelos y Base
# try:
#     from app.models.Users import User
#     from app.models.Roles import Role
#     from app.models.Permissions import Permission
#     from app.models.Role_Permissions import roles_permissions
#     from app.models.Sales import Sale
#     from app.database.connection import Base, SQLALCHEMY_DATABASE_URL
# except ImportError as e:
#     print(f"Error al importar: {e}")
#     print(f"sys.path: {sys.path}")
#     raise

# config = context.config

# if config.config_file_name is not None:
#     fileConfig(config.config_file_name)

# target_metadata = Base.metadata

# config.set_main_option("sqlalchemy.url", SQLALCHEMY_DATABASE_URL)

# def run_migrations_offline() -> None:
#     url = config.get_main_option("sqlalchemy.url")
#     context.configure(
#         url=url,
#         target_metadata=target_metadata,
#         literal_binds=True,
#         dialect_opts={"paramstyle": "named"},
#     )

#     with context.begin_transaction():
#         context.run_migrations()

# def run_migrations_online() -> None:
#     """Run migrations in 'online' mode."""
#     connectable = engine_from_config(
#         config.get_section(config.config_ini_section),
#         prefix="sqlalchemy.",
#         poolclass=pool.NullPool,
#     )

#     with connectable.connect() as connection:
#         context.configure(
#             connection=connection, target_metadata=target_metadata
#         )

#         with context.begin_transaction():
#             context.run_migrations()

# if context.is_offline_mode():
#     run_migrations_offline()
# else:
#     run_migrations_online()