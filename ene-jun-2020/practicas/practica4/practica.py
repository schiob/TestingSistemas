def getHorario(req_user, mat, repo):
    # Check req_user
    if repo.IsAdmin(req_user):
        horario = repo.GetHorario(mat)

        return horario

    return "intruso"