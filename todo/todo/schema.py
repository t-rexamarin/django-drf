import graphene
from graphene import ObjectType
from graphene_django import DjangoObjectType

# from todo.schemas.projects_schema import ProjectUpdateMutation  # дает ошибку
from usersapp.models import User
from project.models import Project, Todo


# 1
# class Query(ObjectType):
#     hello = graphene.String(default_value='Hi!')
#
#
# schema = graphene.Schema(query=Query)


# 2
# class UserType(DjangoObjectType):
#     class Meta:
#         model = User
#         fields = '__all__'
#
#
# class Query(ObjectType):
#     users = graphene.List(UserType)
#
#     def resolve_users(root, info):
#         return User.objects.all()
#
#
# schema = graphene.Schema(query=Query)


# 3
# class ProjectType(DjangoObjectType):
#     class Meta:
#         model = Project
#         fields = '__all__'
#
#
# class UserType(DjangoObjectType):
#     class Meta:
#         model = User
#         fields = '__all__'
#
#
# class Query(ObjectType):
#     users = graphene.List(UserType)
#     projects = graphene.List(ProjectType)
#
#     def resolve_users(root, info):
#         return User.objects.all()
#
#     def resolve_projects(root, info):
#         return Project.objects.all()
#
# # обратная связь юзер-проект
# # {
# #   users {
# #     id
# #     projectSet {  # Set - обращение к связанным проектам, не ко всем
# #       id
# #     }
# #   }
# # }
#
# # {
# #   projects
# #   {
# #     name
# #     users {
# #       username
# #     }
# #   }
# # }
#
# schema = graphene.Schema(query=Query)


# 4
# class ProjectType(DjangoObjectType):
#     class Meta:
#         model = Project
#         fields = '__all__'
#
#
# class UserType(DjangoObjectType):
#     class Meta:
#         model = User
#         fields = '__all__'
#
#
# class Query(ObjectType):
#     user_id = graphene.Field(UserType, id=graphene.Int())
#
#     def resolve_user_id(root, info, id=None):
#         try:
#             return User.objects.get(id=id)
#         except User.DoesNotExist:
#             return None
#
#         # {
#         # 	userId(id:200) {
#         # 	  id
#         #     firstName
#         #     lastName
#         # 	}
#         # }
#
#     projects_by_user = graphene.List(ProjectType, first_name=graphene.String(required=False))
#
#     def resolve_projects_by_user(root, info, first_name=None):
#         projects = Project.objects.all()
#
#         if first_name:
#             projects = projects.filter(users__first_name=first_name)
#         return projects
#
#         # {
#         #     projectsByUser(firstName: "Eric") {
#         #     id
#         # name
#         # }
#         # }
#
#
# schema = graphene.Schema(query=Query)


# 5
class ProjectType(DjangoObjectType):
    class Meta:
        model = Project
        fields = '__all__'


class TodoType(DjangoObjectType):
    class Meta:
        model = Todo
        fields = '__all__'


class UserType(DjangoObjectType):
    class Meta:
        model = User
        fields = '__all__'


class Query(ObjectType):
    user_id = graphene.Field(UserType, id=graphene.Int())

    def resolve_user_id(root, info, id=None):
        try:
            return User.objects.get(id=id)
        except User.DoesNotExist:
            return None

    projects_by_user = graphene.List(ProjectType, first_name=graphene.String(required=False))

    def resolve_projects_by_user(root, info, first_name=None):
        projects = Project.objects.all()

        if first_name:
            projects = projects.filter(users__first_name=first_name)
        return projects

    todos_by_project = graphene.List(TodoType,
                                     project=graphene.Int(required=True),
                                     owner=graphene.Int(required=False))

    def resolve_todos_by_project(root, info, project, owner=None):
        todos = Todo.objects.filter(project=project)

        if owner:
            todos = todos.filter(owner=owner)
        return todos

        # {
        #     todosByProject(project: 28, owner: 200) {
        #     id
        # text
        # owner
        # {
        #     id
        # username
        # }
        # }
        # }


# обновление объекта
class UserUpdateMutation(graphene.Mutation):
    class Arguments:
        birthday_date = graphene.DateTime(required=True)
        id = graphene.ID()

    user = graphene.Field(UserType)

    @classmethod
    def mutate(cls, root, info, birthday_date, id):
        user = User.objects.get(id=id)
        user.birthday_date = birthday_date
        user.save()
        return UserUpdateMutation(user=user)


# создание объекта
# мы не задаем пароль, и узер создастся
class UserCreateMutation(graphene.Mutation):
    class Arguments:
        username = graphene.String()
        first_name = graphene.String()
        last_name = graphene.String()
        email = graphene.String()
        birthday_date = graphene.DateTime(required=True)

    user = graphene.Field(UserType)

    @classmethod
    def mutate(cls, root, info, username, first_name, last_name, email, birthday_date):
        user = User.objects.create_user(
            username=username,
            first_name=first_name,
            last_name=last_name,
            birthday_date=birthday_date,
            email=email
        )

        return UserCreateMutation(user=user)

        # mutation
        # createUser
        # {
        #     createUser(
        #         username: "graphqlUser",
        #     firstName: "graphqlUser",
        #     lastName: "graphqlUser",
        #     email: "graphqlUser@ss.ss",
        #     birthdayDate: "3000-09-13T02:15:28+04:00"){
        #     user
        # {
        #     id
        # username
        # firstName
        # lastName
        # email
        # birthdayDate
        # }
        # }
        # }


# удаление
class UserDeleteMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID()

    user = graphene.Field(UserType)

    @classmethod
    def mutate(cls, root, info, id):
        User.objects.get(id=id).delete()
        return UserDeleteMutation(user=None)

        # mutation
        # deleteUser
        # {
        #     deleteUser(id: 237)
        # {
        #     user
        # {
        #     id
        # }
        # }
        # }


# создание проекта
class ProjectCreateMutation(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        link = graphene.String(required=False)
        users = graphene.List(graphene.Int, required=True)
        # is_active = graphene.Boolean(default_value=1)

    project = graphene.Field(ProjectType)

    @classmethod
    def mutate(cls, root, info, name, link, users):
        project = Project()
        project.name = name
        project.link = link
        project.save()
        project.users.set(users)
        return ProjectCreateMutation(project=project)

        # mutation
        # create_project
        # {
        #     createProject(name: "New project", link: "http://new-project.com", users: [200, 219, 227])
        # {
        #     project
        # {
        #     id
        # name
        # link
        # users
        # {
        #     id
        # username
        # }
        # isActive
        # }
        # }
        # }


# обновление проекта
class ProjectUpdateMutation(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        id = graphene.ID()

    project = graphene.Field(ProjectType)

    @classmethod
    def mutate(cls, root, info, name, id):
        project = Project.objects.get(id=id)
        project.name = name
        project.save()
        return ProjectUpdateMutation(project=project)

        # mutation
        # project_update
        # {
        #     projectUpdate(id: 28, name: "Bates-Koch-Updated")
        # {
        #     project
        # {
        #     id
        # name
        # }
        # }
        # }


class TodoCreateMutation(graphene.Mutation):
    class Arguments:
        project = graphene.ID(required=True)
        text = graphene.String()
        owner = graphene.ID(required=True)
        is_active = graphene.Boolean(default_value=1)

    todo = graphene.Field(TodoType)

    @classmethod
    def mutate(cls, root, info, project, owner, text, is_active):
        todo = Todo.objects.create(
            project=Project.objects.get(id=project),  # т.к. необходим инстанс, а не id
            text=text,
            owner=User.objects.get(id=owner),  # т.к. необходим инстанс, а не id
            is_active=is_active
        )

        return TodoCreateMutation(todo=todo)


class Mutations(ObjectType):
    update_user = UserUpdateMutation.Field()
    create_user = UserCreateMutation.Field()
    delete_user = UserDeleteMutation.Field()

    create_project = ProjectCreateMutation.Field()
    update_project = ProjectUpdateMutation.Field()

    create_todo = TodoCreateMutation.Field()


schema = graphene.Schema(query=Query, mutation=Mutations)
